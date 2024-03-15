import boto3

# Initialize AWS DynamoDB resource
dynamodb = boto3.resource('dynamodb', region_name='local')

def clear_users_table():
    """
    Clear all entries from the Users table.
    """
    users_table = dynamodb.Table('Users')
    response = users_table.scan()
    items = response['Items']
    with users_table.batch_writer() as batch:
        for item in items:
            batch.delete_item(Key={'user_id': item['user_id']})

def clear_transactions_table():
    """
    Clear all entries from the Transactions table.
    """
    transactions_table = dynamodb.Table('Transactions')
    response = transactions_table.scan()
    items = response['Items']
    with transactions_table.batch_writer() as batch:
        for item in items:
            batch.delete_item(Key={'transaction_id': item['transaction_id']})

if __name__ == "__main__":
    clear_users_table()
    clear_transactions_table()
    print("Users and transactions cleared successfully.")
