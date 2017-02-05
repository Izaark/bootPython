from model import Model
class Message(Model):
	def __init__(self,database,collection_name):
		super(Message,self).__init__(database,collection_name)
	
	def delete_collection(self):
		self.collection.delete_many({})
		
