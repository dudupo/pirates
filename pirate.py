


class pirate ():
	def __init__(self ,location ,_id):
		self.location = location
		self.lastlocation = location
		self.id = _id
	
	def __radd__(self , newlocation):
		self.lastlocation = self.location
		self.location = newlocation