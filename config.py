import os
class Config(object):
	SECRET_KEY = 'my_token'
	PAGE_ACCES_TOKEN = 'EAACyBWgWn4ABAElDceHnjl1HnjeXU2xNLKYoI6tHUTj0AS6rZCSKX6eYdKr7VQvzBaeZAtCGZBsFMySPA2DrDWAzh39Xfq32pefvh0r5G1ri74JVmfdYzKlBy4WX7LaMFx87rS9qKGMTZAnjaL5kJKfc4IWOQRyGpERKqzWkLQZDZD'

class DevelopmentConfig(Config):
	DEBUG = True