# Payment Service

The Payment Service helps users with secure transactions. It uses gRPC for communication, Protocol Buffers for messages, and AWS DynamoDB for data storage. This README explains how it works.

## System Architecture

The Payment Service has a gRPC server for making payments, checking account balances, and viewing transaction history. Clients talk to the server using gRPC, which is fast and good for communication between systems.

## Setup

Setting Up and Using the Payment Service
Follow these steps to set up and use the Payment Service:

#### Install Dependencies:
1. python3x
2. grpcio
3. boto3
3. protobuf

### Clone the Repository:
#### Copy the Code

To copy the code clone the repository.

```git clone https://github.com/amnrandh/grpc-payment-service```

#### Start the Payment Service Server:
Start the payment service by running the command below.

```python payment_server.py```

The **payment_server.py** file contains the implementation of the gRPC server. It defines the service methods for making payments, retrieving account balances, and fetching transaction history. These methods interact with DynamoDB to perform the necessary operations.

#### Execute the Payment Client:

Open a new terminal window and run the payment client to interact with the server:
```python payment_client.py```

The **payment_client.py** file provides a simple gRPC client for interacting with the service. It demonstrates how to create gRPC stubs and make RPC calls to the server to perform various actions.

#### Running Unit Tests:
To run unit tests, use the following command:

```python -m unittest test_payment.py```


#### Running End-to-End Tests:

To run end-to-end tests, use the following command:
```pytest test_end_to_end.py```

This will execute all end-to-end tests in the project, ensuring the reliability and correctness of the Payment Service.

By following these steps, you can set up the Payment Service, interact with it using the payment client, and ensure its functionality through unit tests and end-to-end tests.

#### Protocol Buffers: 

The **payment_messages.proto** file defines the message formats used in the communication between the client and server. It specifies the service interface and the structure of request and response messages.

## Technology Choices

### gRPC

We use gRPC because it's fast, easy to use, and works with different languages. It helps define service methods using Protocol Buffers, making communication efficient. gRPC also supports streaming RPCs, useful for getting transaction history.

### Protocol Buffers (protobuf)

Protocol Buffers help define service methods and message types. They make data serialization easy and work across different languages and platforms.

### AWS DynamoDB

We chose AWS DynamoDB for storing user accounts and transactions. It's scalable, reliable, and fast, making it great for handling financial data.

## Payment Implementation

The payment system has methods for different tasks:

### MakePayment Method

Handles payment requests by updating balances and recording transactions in DynamoDB. It ensures data consistency by checking balances and recording transactions together.

### GetAccountBalance Method

Gets the account balance from DynamoDB in real-time, letting clients see their current balance.

### GetTransactionHistory Method

Gets a user's transaction history from DynamoDB, streaming data to the client for easy access.

### AddAccount Method

Adds a new account to DynamoDB, checking for existing accounts first to keep data clean.

## Testing

We test the Payment Service thoroughly to make sure it works well. We use unit tests to check individual parts and end-to-end tests to test the whole system, including DynamoDB interactions.

## Conclusion

The Payment Service is reliable and efficient for handling transactions and managing accounts. With gRPC, Protocol Buffers, and AWS DynamoDB, it provides a scalable platform for payments in any environment.
