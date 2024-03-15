import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
from payment import Payment
from payment_messages_pb2 import Transaction, User, PaymentRequest, PaymentResponse

class TestPayment(unittest.TestCase):
    def setUp(self):
        self.payment = Payment()
        self.mock_users_table = MagicMock()
        self.mock_transactions_table = MagicMock()
        self.payment.users_table = self.mock_users_table
        self.payment.transactions_table = self.mock_transactions_table

    def test_make_payment_with_insufficient_funds(self):
        # Mock the DynamoDB get_item method to return a user with insufficient funds
        self.mock_users_table.get_item.return_value = {'Item': {'balance': 100}}
        
        request = PaymentRequest(sender_id='sender123', recipient_id='recipient456', amount=200)
        response = self.payment.MakePayment(request, None)
        
        self.assertEqual(response.message, "Insufficient funds")

    def test_make_payment_successful(self):
        # Mock the DynamoDB get_item method to return sender and recipient balances
        self.mock_users_table.get_item.side_effect = [
            {'Item': {'balance': 200}},
            {'Item': {'balance': 300}}
        ]
        
        # Mock the DynamoDB update_item method
        self.mock_users_table.update_item.side_effect = [None, None]
        
        request = PaymentRequest(sender_id='sender123', recipient_id='recipient456', amount=100)
        response = self.payment.MakePayment(request, None)
        
        self.assertEqual(response.message, "Payment successful")

    def test_get_transaction_history(self):
        # Mock the DynamoDB query method to return a response
        self.mock_transactions_table.query.return_value = {'Items': [{'transaction_id': '123', 'sender_id': 'sender123', 'recipient_id': 'recipient456', 'amount': 100}]}
        
        request = User(user_id='user123')
        transactions = list(self.payment.GetTransactionHistory(request, None))
        
        self.assertEqual(len(transactions), 2)
        self.assertIsInstance(transactions[0], Transaction)

    def test_get_account_balance(self):
        # Mock the DynamoDB get_item method to return a user's balance
        self.mock_users_table.get_item.return_value = {'Item': {'balance': 500}}
        
        request = User(user_id='user123')
        user = self.payment.GetAccountBalance(request, None)
        
        self.assertEqual(user.balance, 500)

    def test_record_transaction(self):
        # Mock the generate_transaction_id method
        with patch.object(self.payment, '_generate_transaction_id') as mock_generate_transaction_id:
            mock_generate_transaction_id.return_value = 'mock_transaction_id'

            # Act
            self.payment._record_transaction('sender123', 'recipient456', 100)

            # Assert
            self.mock_transactions_table.put_item.assert_called_once_with(Item={
                'transaction_id': 'mock_transaction_id',
                'sender_id': 'sender123',
                'recipient_id': 'recipient456',
                'amount': 100
            })

    def test_add_account(self):
        # Mock the DynamoDB get_item method to return 0 balance, indicating account doesn't exist
        self.mock_users_table.get_item.return_value = {'Item': {'balance': 0}}

        # Mock the DynamoDB update_item method
        self.mock_users_table.update_item.side_effect = [None]
        
        request = User(user_id='user123', balance=100)
        response = self.payment.AddAccount(request, None)
        
        self.assertEqual(response.message, "Account created successfully")

if __name__ == '__main__':
    unittest.main()
