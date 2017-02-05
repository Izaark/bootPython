class Model(object):
	def __init__(self,database,collection_name):
		self.database = database
		self.collection_name = collection_name
		self.collection = database[self.collection_name]

	def new(self,**kwargs):
		self.save(kwargs)
	def save(self,document):
		self.collection.save(document)
	def find(self,**kwargs):
		return self.collection.find_one(kwargs)

