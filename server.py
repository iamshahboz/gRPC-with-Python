import grpc
from concurrent import futures
import calculator_pb2
import calculator_pb2_grpc
import logging

logging.basicConfig(
     filename='grpc.log',
     level=logging.INFO, 
     format= '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
     datefmt='%H:%M:%S'
)

class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    def Add(self, request, context):
        result = request.number1 + request.number2
        return calculator_pb2.AddResponse(result=result)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()





if __name__ == '__main__':
    logging.info('Waiting for client message...')
    serve()