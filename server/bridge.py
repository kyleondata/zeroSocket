import time
import websocket
import zmq
import threading

class bridge():

    context = zmq.Context()
    socketIn = context.socket(zmq.REP)
    socketOut = context.socket(zmq.REQ)

    def _wsToZmqBridge(self):
        time.sleep(1)
        ws = websocket.WebSocket()
        ws.connect("ws://127.0.0.1:9000/test")

        while True:
            message = self.socketIn.recv()
            ws.send(message)
            self.socketIn.send(message)

    def _zmqToWsBridge(self):
        time.sleep(1)
        ws = websocket.WebSocket()
        ws.connect("ws://127.0.0.1:9000/test")

        while True:
            message = ws.recv()
            self.socketOut.send(message)
            self.socketOut.recv()

    def bind(self):
        # Bind zmq sockets
        self.socketIn.bind("tcp://*:5555")
        self.socketOut.bind("tcp://*:5556")

    def startThreads(self):
        wsToZmqThread = threading.Thread(target=self._wsToZmqBridge)
        wsToZmqThread.start();

        zmqToWsThread = threading.Thread(target=self._zmqToWsBridge)
        zmqToWsThread.start();
