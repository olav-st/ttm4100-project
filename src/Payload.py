class Payload(object):
	def __init__(self, type, sender, content):
		self.type = type #string
		self.sender = sender #User
		self.content = content #string
		self.timestamp = 0 #todo

	def getType(self):
		return self.type
	   
	def getSender(self):
		return self.sender

	def getContent(self):
		return self.content
	
	def getTimestampSelf():
		return self.timestamp