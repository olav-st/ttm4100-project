class Server(object):
	def __init__(self, port):
		self.port = port #integer
		self.messages = [] #list of recieved messages
		self.users = [] #list of connected users

	def broadcast(self, payload):
		pass #TODO

	def sendTo(self, reciever, payload):
		pass #TODO

	def recieve(self, sender, payload):
		pass #TODO

	def getPort(self):
		return self.port

	def getMessages(self):
		return self.messages

	def getUsers(self):
		return self.users