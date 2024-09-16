import grpc
import calculator_pb2
import calculator_pb2_grpc
import logging


logging.basicConfig(
     filename='grpc.log',
     level=logging.INFO, 
     format= '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
     datefmt='%H:%M:%S'
)


def run(number1:int, number2:int)->int:
    '''
    Function takes two integers as parameters and 
    returns the Sum of them
    '''
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        response = stub.Add(calculator_pb2.AddRequest(number1=number1, number2=number2))
    
    print(f"Result: {response.result}")
    logging.info('The result is printed in console')




if __name__ == '__main__':
    number1 = int(input("Please input first number: "))
    number2 = int(input("Please input second number: "))
    run(number1, number2)