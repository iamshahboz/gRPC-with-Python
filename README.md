## gRPC with Python


### If you want to create other implementation with gRPC you should do the following

1. Modify file calculator.proto
2. generate gRPC files with the following command
```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto
```
3. change the server.py and client.py accordingly

## Running
### In two separate terminals run

1. 
```bash
python server.py
```
2. 
```bash
python client.py
```

