# -*- coding: utf-8 -*-
import socketserver as SocketServer
import json

class ClientHandler(SocketServer.BaseRequestHandler):
	"""
	This is the ClientHandler class. Everytime a new client connects to the
	server, a new ClientHandler object will be created. This class represents
	only connected clients, and not the server itself. If you want to write
	logic for the server, you must write it outside this class
	"""

	def handle(self):
		"""
		This method handles the connection between a client and the server.
		"""
		self.ip = self.client_address[0]
		self.port = self.client_address[1]
		self.connection = self.request
		self.user = None
		connections.append(self)
		
		# Loop that listens for messages from the client
		while True:
			recv = json.loads(self.connection.recv(4096).decode('utf-8'))
			if(recv['request'] == 'login'):
				self.login(recv)
			elif(recv['request'] == 'logout'):
				if(self.user == None):
					self.error('Not logged in')
				else:
					self.logout()
			elif(recv['request'] == 'msg'):
				if(self.user == None):
					self.error('Not logged in')
				else:
					self.message(recv)
				pass
			elif(recv['request'] == 'names'):
				if(self.user == None):
					self.error('Not logged in')
				else:
					self.names()
			elif(recv['request'] == 'help'):
				self.help()
				pass
			else:
				if(self.user == None):
					self.error('Unknown request')
				pass
			# TODO: Add handling of received payload from client
	
	def login(self, recv):
		#TODO validate username
		print(recv['content'],'logged in')
		self.user = recv['content']
		
	def logout(self):
		#todo
		connections.remove(self)
		pass
		
	def message(self, recv):
		payload=json.dumps({'timestamp': 0, 'sender': self.user, 'response': 'msg', 'content': recv['content']})	
		for connected in connections:
			connected.send_payload(payload)
	
	def names(self):
		#todo
		pass
		
	def help(self):
		payload=json.dumps({'timestamp': 0, 'sender': '[Help]', 'response': 'info', 'content': 'This is a server'})
		self.send_payload(payload)
		
	def send_payload(self, data):
		# TODO: Handle sending of a payload
		self.connection.send(bytes(data, 'UTF-8'))
		pass
		
	def error(self, msg):
		payload=json.dumps({'timestamp': 0, 'sender': '[Error}]', 'response': 'error', 'content': msg})
		self.send_payload(payload)

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
	"""
	This class is present so that each client connected will be ran as a own
	thread. In that way, all clients will be served by the server.

	No alterations is necessary
	"""
	allow_reuse_address = True

if __name__ == "__main__":
	"""
	This is the main method and is executed when you type "python Server.py"
	in your terminal.

	No alterations is necessary
	"""
	HOST, PORT = 'localhost', 9998
	print('Server running...')
	
	connections=[]
	messages=[]
	
	# Set up and initiate the TCP server
	server = ThreadedTCPServer((HOST, PORT), ClientHandler)
	server.serve_forever()
