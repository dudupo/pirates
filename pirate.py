


class pirate():
	def __init__(self ,player ,location ,_id ,fireRange , speed):
		self.location = location
		self.id = _id
		self.fireRange = fireRange
		self.speed = speed
		self.power = speed
		self.player =  player
		self.alive = True
		self.timeToDiead = 40 
	def __str__(self):
		return ">>>pirate: " + str(self.id) + "\n   location: " + str(self.location)

