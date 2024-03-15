import pytest
import grpc
from payment_messages_pb2 import PaymentRequest, User
from payment_pb2_grpc import PaymentStub
from server import serve
from payment_pb2_grpc import add_PaymentServicer_to_server

@pytest.fixture(scope="module")
def grpc_channel():
    print("Setting up gRPC channel...")
    channel = grpc.insecure_channel('localhost:50051')
    yield channel
    print("Tearing down gRPC channel...")

@pytest.fixture(scope="module")
def grpc_stub(grpc_channel):
    print("Creating gRPC stub...")
    stub = PaymentStub(grpc_channel)
    yield stub
    print("Tearing down gRPC stub...")

def add_accounts(grpc_stub):
    print("Adding sender and recipient accounts...")
    # Add sender account
    sender_request = User(user_id='sender123')
    grpc_stub.AddAccount(sender_request)
    
    # Add recipient account
    recipient_request = User(user_id='recipient456')
    grpc_stub.AddAccount(recipient_request)

def test_make_payment(grpc_stub):
    print("Running test: test_make_payment...")
    # Add accounts before making the payment
    add_accounts(grpc_stub)
    
    # Make the payment
    request = PaymentRequest(sender_id='sender123', recipient_id='recipient456', amount=float(100))
    response = grpc_stub.MakePayment(request)
    print("Payment response:", response)


def test_get_account_balance(grpc_stub):
    print("Running test: test_get_account_balance...")
    request = User(user_id='user123')
    user = grpc_stub.GetAccountBalance(request)
    print("Account balance:", user.balance)

def test_get_transaction_history(grpc_stub):
    print("Running test: test_get_transaction_history...")
    request = User(user_id='user123')
    transactions = grpc_stub.GetTransactionHistory(request)
    print("Transaction history:")
    for transaction in transactions:
        print(transaction)

if __name__ == "__main__":
    serve()
