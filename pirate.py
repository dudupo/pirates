class Pirate():
	i=0
	def __init__(self ,player ,location ,_id):
		self.location = location
		self.id = _id
		self.player =  player
		player._add_pirate(self)
		self.alive = True
		self.respawn_time = 10
		self.turns_dead=0
		self.spawnpoint = player.spawn_area[self.id]
		self.fire_range=5
		
		self.uniq=Pirate.i
		Pirate.i+=1
	def __str__(self):
		return "p" + str(self.uniq)

