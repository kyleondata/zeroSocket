import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)

# open zmg connection
socket.connect("tcp://localhost:5555")

while True:
    msg = raw_input()
    socket.send(msg)
    reply = socket.recv()
