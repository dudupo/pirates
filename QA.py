
import engine 
from bot import Bot
from vector import Vector

engine.init(["miki","dani"])



for i in range(200):
	for bot in engine.bots:
		bot()
	engine.update() 

