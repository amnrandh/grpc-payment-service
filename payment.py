import boto3
import time
import uuid
from payment_messages_pb2 import Transaction, User, PaymentResponse

# Initialize AWS DynamoDB resource
dynamodb = boto3.resource('dynamodb', region_name='local')

class Payment:
    def __init__(self):
        # Connect to DynamoDB tables
        self.users_table = dynamodb.Table('Users')
        self.transactions_table = dynamodb.Table('Transactions')

    def MakePayment(self, request, context):
        """
        Process payment request:
        - Update sender and recipient account balances
        - Record transaction in DynamoDB
        """
        # Extract payment details from request
        sender_id = request.sender_id
        recipient_id = request.recipient_id
        amount = request.amount
        
        # Log the received request data
        print("Received payment request:", request)
        # Retrieve sender and recipient account balances from DynamoDB
        sender_balance = self._get_account_balance(sender_id)
        recipient_balance = self._get_account_balance(recipient_id)
        
        # Check if sender has sufficient funds
        if sender_balance < amount:
            # Construct a response indicating insufficient funds
            print("Insufficient funds:", request)
            return PaymentResponse(message="Insufficient funds")

        # Update sender and recipient balances
        sender_balance -= amount
        recipient_balance += amount

        # Record transaction in DynamoDB
        transaction_id = self._record_transaction(sender_id, recipient_id, amount)

        # Update account balances in DynamoDB
        self._update_account_balance(sender_id, str(sender_balance))  # Convert to string
        self._update_account_balance(recipient_id, str(recipient_balance))  # Convert to string

        # Return successful payment response
        return PaymentResponse(message="Payment successful")

    def GetAccountBalance(self, request, context):
        """
        Retrieve account balance for a user.
        """
        user_id = request.user_id

        # Get user's account balance from DynamoDB
        balance = self._get_account_balance(user_id)

        # Return user's account balance
        return User(user_id=user_id, balance=float(balance))  # Convert to float

    def GetTransactionHistory(self, request, context):
        """
        Retrieve transaction history for a user.
        Stream transactions to the client.
        """
        user_id = request.user_id

        # Query DynamoDB for sender transactions
        sender_transactions = self.transactions_table.query(
            IndexName='sender_index',  # Assuming 'sender_index' is a global secondary index on the 'Transactions' table with 'sender_id' as the partition key
            KeyConditionExpression='sender_id = :user_id',
            ExpressionAttributeValues={':user_id': user_id}
        )

        # Query DynamoDB for recipient transactions
        recipient_transactions = self.transactions_table.query(
            IndexName='recipient_index',  # Assuming 'recipient_index' is a global secondary index on the 'Transactions' table with 'recipient_id' as the partition key
            KeyConditionExpression='recipient_id = :user_id',
            ExpressionAttributeValues={':user_id': user_id}
        )

        # Combine sender and recipient transactions
        all_transactions = sender_transactions['Items'] + recipient_transactions['Items']

        # Stream transactions to the client
        for item in all_transactions:
            yield Transaction(transaction_id=item['transaction_id'], sender_id=item['sender_id'],
                            recipient_id=item['recipient_id'], amount=float(item['amount']))  # Convert to float

    def AddAccount(self, request, context):
        """
        Add a new account with the specified user ID and initial balance.
        """
        user_id = request.user_id
        initial_balance = request.balance

        
        # Check if the account already exists
        if self._get_account_balance(user_id) != 0:
            print("Account already exists for user:", user_id)
            return PaymentResponse(message="Account already exists")

        # Create the new account
        self._update_account_balance(user_id, str(initial_balance))  # Convert to string
        print("New account created for user:", user_id)
        return PaymentResponse(message="Account created successfully")

    def _get_account_balance(self, user_id):
        """
        Retrieve account balance for a user from DynamoDB.
        """
        response = self.users_table.get_item(Key={'user_id': user_id})
        item = response.get('Item')
        if item:
            return float(item.get('balance', 0))  # Convert to float
        else:
            return 0

    def _update_account_balance(self, user_id, balance):
        """
        Update account balance for a user in DynamoDB.
        """
        self.users_table.update_item(
            Key={'user_id': user_id},
            UpdateExpression='SET balance = :balance',
            ExpressionAttributeValues={':balance': balance}
        )
        
    def _generate_transaction_id(self, sender_id, recipient_id):
        """
        Generate a unique transaction ID.
        """
        timestamp = int(time.time() * 1000)  # Current timestamp in milliseconds
        unique_id = uuid.uuid4().hex  # Generate a random UUID
        return f"{sender_id}-{recipient_id}-{timestamp}-{unique_id}"

        
    def _record_transaction(self, sender_id, recipient_id, amount):
        """
        Record transaction in DynamoDB.
        """
        transaction_id = self._generate_transaction_id(sender_id, recipient_id)
        self.transactions_table.put_item(Item={
            'transaction_id': transaction_id,
            'sender_id': sender_id,
            'recipient_id': recipient_id,
            'amount': int(amount)  # Convert to integer
        })
