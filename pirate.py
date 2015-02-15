class pirate():
	def __init__(self ,player ,location ,_id):
		self.location = location
		self.id = _id
		self.player =  player
		player._add_pirate(self)
		self.alive = True
		self.respawn_time = 40
		self.turns_dead=0
		self.spawnpoint = player.spawn_area[self.id]
		self.fire_range=5
	def __str__(self):
		return "pirate n" + str(self.id)

