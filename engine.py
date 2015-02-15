from vector import Vector
from player import Player
from game import Game
from pirate import Pirate
from bot import Bot
import datetime
pirates = []
living_pirates=pirates 
dead_pirates=[]

players = []
games={}
bots=[]

islands=[]
island_areas=list()
for island in islands:
	island_areas+=islands.area

score_table= {}
for player in players:
	score_table[player]=0

tasks=[]

boardsize=Vector(50,50)
def onboard(location):
	'returns true if the location is posiotioned on the board'
	return not (location.x <0 or location.x >= boardsize.x or \
		location.y <0 or location.y >= boardsize.y) 

def init(playernames):
	f = open('log.txt', 'w')
	f.write("GAME BETWEEN {}\n\n".format(playernames))
	for name, pid in zip(playernames,range(len(playernames))):
		newplayer=Player(name,pid)
		players.append(newplayer)
		newgame=Game(newplayer)
		games[newplayer]=newgame
		bots.append(Bot("bots."+name,newgame))
		for x in range(Game.MAX_AMOUNT_OF_PIRATES):
			newpirate = Pirate(newplayer,newplayer.spawn_area[x],x)
			pirates.append(newpirate)
			living_pirates.append(newpirate)
			bind_pirate(newpirate)


def bind_pirate(pirate):
	'binds pirate "pirate" to the game'
	if not onboard(pirate.location):
		raise Exception("you are trying to bind a {} that is outisde the board".format(pirate.location))
	pirates.append(pirate)
	drawmap[(pirate.location.x,pirate.location.y)]=pirate.player.sign
def spawn_pirate(pirate):
	dead_pirates.remove(pirate)
	living_pirates.append(pirate)
def kill_pirate(pirate):
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
	for (taskname, pirate, direaction) in tasks:
		if didnt_move[pirate]:
			newlocation = pirate.location+direaction
			if onboard(newlocation):
				if (newlocation not in island_areas):
					last =drawmap[(pirate.location.x,pirate.location.y)]
					drawmap[(pirate.location.x,pirate.location.y)]='.'
					pirate.location=newlocation
					drawmap[(pirate.location.x,pirate.location.y)]=last
				else:
					print("WORNING: {} tried to move inside an island".format(pirate))
			else:
				print("WORNING: {} tried to move outise the map".format(pirate))
		else:
			print("WORNING: {} tried to move twice or more at the same turn".format(pirate))
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
def cap():
	for island in islands:
		for pirate in living_pirates:
			island._try_cap(pirate)

def update():
	global tasks
	try_to_revive()
	move(tasks)
	battle()
	cap()
	tasks=[]
	draw()
drawmap={}
def draw():
	todorw=""
	for y in range(boardsize.y):
		for x in range(boardsize.x):
			try:
				ch = drawmap[(x,y)]
			except:
				if (x,y) in island_areas:
					ch='O'
				else:
					ch='.'
			todorw+=ch
		todorw+='\n'

	f = open('log.txt', 'a')
	f.write((todorw)+"\n")
	f.close()