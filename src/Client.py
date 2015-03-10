import Payload
from socket import *

class Client(object):
	def __init__(self, server_ip, server_port):
		self.server_ip = server_ip
		self.server_port = server_port
		
		clientSocket = socket()
		clientSocket.connect((server_ip, server_port))
		clientSocket.setblocking(0)

	def login(self, user):
		pass #todo
		
	def logout(self):
		pass #todo
	
	def send(self, payload):
		pass #todo
		
	def receive(self, payload):
		
		pass #todo