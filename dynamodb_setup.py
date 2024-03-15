import boto3

# Create a boto3 session with the appropriate AWS credentials and region
session = boto3.Session(
    aws_access_key_id='fakeAccessKey',
    aws_secret_access_key='fakeSecretAccessKey',
    region_name='local'
)

# Create a DynamoDB resource object with the specified endpoint URL
dynamodb = session.resource('dynamodb')

# Define the table names
USERS_TABLE_NAME = 'Users'
TRANSACTIONS_TABLE_NAME = 'Transactions'

# Define the table schemas
users_table_schema = {
    'TableName': USERS_TABLE_NAME,
    'KeySchema': [
        {
            'AttributeName': 'user_id',
            'KeyType': 'HASH'
        }
    ],
    'AttributeDefinitions': [
        {
            'AttributeName': 'user_id',
            'AttributeType': 'S'
        }
    ],
    'ProvisionedThroughput': {
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
}

transactions_table_schema = {
    'TableName': TRANSACTIONS_TABLE_NAME,
    'KeySchema': [
        {
            'AttributeName': 'transaction_id',
            'KeyType': 'HASH'
        }
    ],
    'AttributeDefinitions': [
        {
            'AttributeName': 'transaction_id',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'sender_id',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'recipient_id',
            'AttributeType': 'S'
        }
    ],
    'ProvisionedThroughput': {
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    },
    'GlobalSecondaryIndexes': [
        {
            'IndexName': 'sender_index',
            'KeySchema': [
                {
                    'AttributeName': 'sender_id',
                    'KeyType': 'HASH'
                }
            ],
            'Projection': {
                'ProjectionType': 'ALL'
            },
            'ProvisionedThroughput': {
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        },
        {
            'IndexName': 'recipient_index',
            'KeySchema': [
                {
                    'AttributeName': 'recipient_id',
                    'KeyType': 'HASH'
                }
            ],
            'Projection': {
                'ProjectionType': 'ALL'
            },
            'ProvisionedThroughput': {
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        }
    ]
}

# Create the DynamoDB tables
try:
    users_table = dynamodb.create_table(**users_table_schema)
    print(f"Table '{USERS_TABLE_NAME}' created successfully.")
except dynamodb.meta.client.exceptions.ResourceInUseException:
    print(f"Table '{USERS_TABLE_NAME}' already exists.")

try:
    transactions_table = dynamodb.create_table(**transactions_table_schema)
    print(f"Table '{TRANSACTIONS_TABLE_NAME}' created successfully.")
except dynamodb.meta.client.exceptions.ResourceInUseException:
    print(f"Table '{TRANSACTIONS_TABLE_NAME}' already exists.")
