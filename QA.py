
import engine 
from bot import Bot
from vector import Vector

engine.init(["miki","dani"])


def winner():
	WINNING_SCORE=1000
	for player, score in engine.score_table.items():
		if score>=WINNING_SCORE:
			return player
	return None
for i in range(200):
	if i%50==0:
		print("Turn {} {} ".format(i,engine.pscore()))
	if winner() !=None:
		print(str(winner())+" wins!")
		break
	
	for bot in engine.bots:
		try:
			bot()
		except:
			print(bot.game.player.name+" is out of the game due to exception")
			engine.remove(bot)
	
	if len(engine.bots)==1:
		print(engine.bots[0].player.name+" wins!")
		break
	
	engine.update() 

