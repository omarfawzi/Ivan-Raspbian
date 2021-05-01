from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

clients = []
port = 9090


class SimpleChat(WebSocket):

    def handleMessage(self):
        for client in clients:
            if client != self:
                client.sendMessage(self.data)

    def handleConnected(self):
        clients.append(self)

    def handleClose(self):
        clients.remove(self)


server = SimpleWebSocketServer('', port, SimpleChat)

print('Running websocket over port : {port}'.format(port=port))

server.serveforever()
