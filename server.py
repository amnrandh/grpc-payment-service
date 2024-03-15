import grpc
import payment_pb2_grpc
from payment_messages_pb2 import PaymentRequest, Transaction, User, PaymentResponse
from payment import Payment

from concurrent import futures

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    payment_pb2_grpc.add_PaymentServicer_to_server(Payment(), server)
    server.add_insecure_port('localhost:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
