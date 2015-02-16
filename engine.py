from vector import Vector
from player import Player
from game import Game
from pirate import Pirate
from bot import Bot
import datetime
from island import Island

pirates = []
living_pirates=[]
dead_pirates=[]

players = []
games={}
bots=[]
boardsize=Vector(171,40)

islands=[
	Island(Vector(int(boardsize.x/2)+1,int(boardsize.y*3/4)+1)),
	Island(Vector(int(boardsize.x/4)+1,int(boardsize.y/2)+1)),
	Island(Vector(int(boardsize.x*3/4)+1,int(boardsize.y/2)+1)),
	Island(Vector(int(boardsize.x*1/3)+1,int(boardsize.y/4)+1)),
	Island(Vector(int(boardsize.x*2/3)+1,int(boardsize.y/4)+1)),
	]

island_areas=list()
for island in islands:
	island_areas+=island.area

score_table= {}


tasks=[]

debug_turn_message=""


def onboard(location):
	'returns true if the location is posiotioned on the board'
	return not (location.x <0 or location.x >= boardsize.x or \
		location.y <0 or location.y >= boardsize.y) 

def init(playernames):
	f = open('.log', 'w')
	f.write("GAME BETWEEN {}\n\n".format(playernames))
	for name, pid in zip(playernames,range(len(playernames))):
		newplayer=Player(name,pid)
		players.append(newplayer)
		newgame=Game(newplayer)
		games[newplayer]=newgame
		bots.append(Bot("bots."+name,newgame))
		for x in range(Game.MAX_AMOUNT_OF_PIRATES):
			newpirate = Pirate(newplayer,newplayer.spawn_area[x],x)
			bind_pirate(newpirate)
	for island in islands:
		island.post_init()
	for player in players:
		score_table[player]=0
def bind_pirate(pirate):
	'binds pirate "pirate" to the game'
	if not onboard(pirate.location):
		raise Exception("you are trying to bind a {} that is outisde the board".format(pirate.location))
	pirates.append(pirate)
	living_pirates.append(pirate)
	drawmap[(pirate.location.x,pirate.location.y)]=pirate.player.sign

def spawn_pirate(pirate):
	print("spawning {} ".format(pirate))
	dead_pirates.remove(pirate)
	living_pirates.append(pirate)
	pirate.location=pirate.spawnpoint
	drawmap[(pirate.location.x,pirate.location.y)]=pirate.player.sign

def kill_pirate(pirate):
	drawmap[(pirate.location.x,pirate.location.y)]='-'
	living_pirates.remove(pirate)
	dead_pirates.append(pirate)
	pirate.turns_dead=0

#stages
def try_to_revive():
	'at the beggining of the turn the engine tries to revive the dead pirates'
	for pirate in dead_pirates:
		pirate.turns_dead+=1
		if pirate.turns_dead >= pirate.respawn_time:
			spawn_pirate(pirate)
def move(tasks):
	'moves all the pirates as requested'
	didnt_move={}
	for pirate in pirates:
		didnt_move[pirate] = pirate.alive

	def retry(mtask):
		for (taskname, pirate, direaction) in mtask:
			fsize=len(mtask)
			#double turn check
			if didnt_move[pirate]:

				newlocation = pirate.location+direaction
				#onboard check
				if onboard(newlocation):
					#island check
					if (newlocation not in island_areas):
						#colision check
						if len([i for i in pirates if i!=pirate and i.location==pirate.location])>0:

							last =drawmap[(pirate.location.x,pirate.location.y)]
							drawmap[(pirate.location.x,pirate.location.y)]='-'
							pirate.location=location
							drawmap[(pirate.location.x,pirate.location.y)]=last

							mtask.remove(pirate)
						else:
							continue
							#print("WORNING: {} tried to move inside of another pirate".format(pirate))
							
					else:
						continue
						#print("WORNING: {} tried to move inside an island".format(pirate))
					
				else:
					continue
					#print("WORNING: {} tried to move outise the map".format(pirate))
					
			else:
					continue
			if len(mtask) ==fsize:
				print("OH Oh")
	for pirate,location in tomove.items():
		
	tasks=[]
def battle():
	attackers={}
	#init attackers list
	for pirate in living_pirates:
		attackers[pirate]=list()
	
	for pirate in living_pirates:
		for other in living_pirates:
			if (other.player!=pirate.player) and (pirate.location.distance_to(other.location) <= pirate.fire_range):
				attackers[other].append(pirate)
	
	for attacked, enemies in attackers.items():
		for enemy in enemies:
			if len(enemies) > len(attackers[enemy]):
				kill_pirate(attacked)
			elif len(enemies) < len(attackers[enemy]):
				kill_pirate(enemy)
			else:
				kill_pirate(enemy)
				kill_pirate(attacked)
				attackers[enemy]=list()
				attackers[attacked]=list()
def cap():
	global debug_turn_message
	for island in islands:
		for pirate in living_pirates:
			for area in island.area:
				if pirate.location.isadj(area):
					debug_turn_message="conenction!"
					island._try_cap(pirate)
						
turn=0
def update():
	global turn
	global tasks
	for island in islands:
		island.onturn()
	
	try_to_revive()
	move(tasks)
	battle()
	
	cap()
	
	tasks=[]
	
	draw()
	turn+=1

drawmap={}
def pscore():
	score=""
	for p in players:
		score+="{}:{} ".format(p.name,score_table[p])
	return score
def draw():
	global turn
	global debug_turn_message
	score=pscore()
	todorw="[TURN {}] {} {}\n\n".format(turn,score,debug_turn_message)
	for y in range(boardsize.y):
		for x in range(boardsize.x):
			try:
				ch = drawmap[(x,y)]
			except:
				if (x,y) in island_areas:
					ch='O'
				else:
					ch='-'
			todorw+=ch
		todorw+='\n'

	f = open('.log', 'a')
	f.write((todorw)+"\n\n\n")
	f.close()
	debug_turn_message=""