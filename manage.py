from flask import Flask
from config import DevelopmentConfig 

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

@app.route('/',methods =['GET'])
def index():
	return 'Hello world'
	
if __name__ == '__main__':
	app.run(port=8000)
