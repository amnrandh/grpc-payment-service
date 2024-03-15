import grpc
import payment_messages_pb2
import payment_pb2_grpc

def run_client():
    # Establish a connection to the gRPC server
    channel = grpc.insecure_channel('localhost:50051')
    
    # Create a gRPC stub
    stub = payment_pb2_grpc.PaymentStub(channel)
    
    # Prepare a request to get the account balance for a user
    user_id = "user123"  # Replace with the actual user ID
    account_balance_request = payment_messages_pb2.User(user_id=user_id)
    
    try:
        # Invoke the GetAccountBalance method
        account_balance_response = stub.GetAccountBalance(account_balance_request)
        
        # Print the account balance
        print(f"Account balance for user {user_id}: {account_balance_response.balance}")
    except grpc.RpcError as e:
        print("Failed to get account balance:", e)

if __name__ == "__main__":
    run_client()
