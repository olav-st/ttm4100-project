import json

class Payload(object):
	def __init__(self, type=None, sender=None, content=None):
		self.type = type #string
		self.sender = sender #User
		self.content = content #string
		self.timestamp = 0 #todo
		
	def parseJson(self, json_string):
		jdata = json.loads(json_string)
		#todo: catch undefined
		self.type = jdata['type']
		self.sender = jdata['sender']
		self.content = jdata['content']
		self.timestamp = jdata['timestamp']

	def getType(self):
		return self.type
	   
	def getSender(self):
		return self.sender

	def getContent(self):
		return self.content
	
	def getTimestampSelf():
		return self.timestamp