import engine
from vector import Vector
class Island:
	EMPTY_CAP_TIME = 20
	TAKEN_CAP_TIME = EMPTY_CAP_TIME
	
	def __init__(self,p):
		self.area=[p,p+Vector(1,0),p+Vector(2,0),p+Vector(0,1),p+Vector(1,1),p+Vector(2,1)]
		self._owner=None
		self.tried_to_cap_this_turn ={}
		self.capscore={}
		
	def post_init(self):
		for player in engine.players:
			self.capscore[player]=0
	def onturn(self):
		if self._owner!=None:
			engine.score_table[self._owner]+=1
		for player in engine.players:
			self.tried_to_cap_this_turn[player]=False
	def get_owner(self):
		return self._owner
	def get_postion(self):
		return self.__posiotin

	def _try_cap(self,pirate):
		if self._owner==pirate.player:
			pass
		
		elif not self.tried_to_cap_this_turn[pirate.player]:
			self.tried_to_cap_this_turn[pirate.player]=True
			#add score on cap
			for player, score in self.capscore.items():
				if  player == pirate.player:
					self.capscore[player]+=1
				else:
					self.capscore[player]=0
			#change owner ship
			if self._owner==None and self.capscore[pirate.player] >= Island.EMPTY_CAP_TIME:
				self._owner=pirate.player
				print("[TURN {}] player {} captured the island {} ".format(engine.turn,pirate.player,self))
				
			elif self._owner!= None and self.capscore[pirate.player] >=Island.TAKEN_CAP_TIME:
				self._owner=None
		else:
			return False
		