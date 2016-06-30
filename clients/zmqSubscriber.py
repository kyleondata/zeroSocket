import zmq
import time
import websocket

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.connect("tcp://localhost:5556")

while True:
    payload = socket.recv()
    print payload
    socket.send(payload)
