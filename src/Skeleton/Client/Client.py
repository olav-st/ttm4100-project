# -*- coding: utf-8 -*-
import socket
from MessageReceiver import MessageReceiver
import json

class Client:
	"""
	This is the chat client class
	"""

	def __init__(self, host, server_port):
		"""
		This method is run when creating a new Client object
		"""

		# Set up the socket connection to the server
		self.host = host
		self.server_port = server_port
		self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.run()

	def run(self):
		# Initiate the connection to the server
		self.connection.connect((self.host, self.server_port))
		self.thread = MessageReceiver(self, self.connection)
		self.thread.start()
		
		while True:
			text = input()
			if(text.split()[0] == 'login'):
				payload=json.dumps({'request': 'login', 'content': text.split()[1]})
				self.send_payload(payload)
			elif(text.split()[0] == 'logout'):
				self.disconnect()
			elif(text.split()[0] == 'names'):
				payload=json.dumps({'request': 'names'})
				self.send_payload(payload)
			elif(text.split()[0] == 'help'):
				payload=json.dumps({'request': 'help'})
				self.send_payload(payload)
			else:
				payload=json.dumps({'request': 'msg', 'content': text})
				self.send_payload(payload)




	def disconnect(self):
		# TODO: Handle disconnection
		payload=json.dumps({'request': 'logout'})
		self.send_payload(payload)

	def receive_message(self, message):
		# TODO: Handle incoming message
		recv=json.loads(message)
		if(recv['response'] == 'info'):
			print('[Info]', recv['content'])
		elif(recv['response'] == 'error'):
			print('[Error]', recv['content'])
		elif(recv['response'] == 'msg'):
			print(recv['sender']+':', recv['content'])
		elif(recv['response'] == 'history'):
			#todo
			pass
		else:
			print('Unknown server message:', recv)
		pass

	def send_payload(self, data):
		self.connection.send(bytes(data, 'UTF-8'))


if __name__ == '__main__':
	"""
	This is the main method and is executed when you type "python Client.py"
	in your terminal.

	No alterations is necessary
	"""
	client = Client('localhost', 9998)
