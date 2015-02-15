
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
for i in range(2000):
	if i%50==0:
		print("turn {}".format(i))
	if winner() !=None:
		print(str(winner())+" wins!")
		break
	for bot in engine.bots:
		bot()
	engine.update() 

