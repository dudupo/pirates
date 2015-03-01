
import engine 
from bot import Bot
from vector import Vector
import outPut
import random 

start = random.choice([True,False])

bots = ["dani" , "bot2"]

if not start :
	bots = [bots[1]] + [bots[0]]
engine.init(bots)


def winner():
	WINNING_SCORE=3000
	for player, score in engine.score_table.items():
		if score>=WINNING_SCORE:
			return player
	return None


for i in range(3000):
	if i%50==0:
		print("Turn {} {} ".format(i,engine.pscore()))
	
	player = winner()
	if player != None:
		print("Turn {} {} ; {} wins! ".format(i,engine.pscore() , player.name))
		break
	
	
	for bot in engine.bots:
		
		try:
			bot()
		except:
			print(bot.game.player.name+" is out of the game due to exception")
			engine.bots.remove(bot)
		
	
	if len(engine.bots)==1:
		print("Turn {} {} ; {} wins! ".format(i,engine.pscore() , engine.bots[0].game.player.name))
		break
	
	engine.update() 

outPut.build()

from os import system 
system("out.html")