
from importlib import import_module

DO_TURN_METHOD_NAME= 'do_turn'
class Bot:
	'A class that represents the function "do_turn" in each bot'
	def __init__(self, name_of_bot ,game):
		mod = import_module(name_of_bot)
		self.do_turn = getattr(mod ,DO_TURN_METHOD_NAME)
		self.game=game
	def __call__(self):
		self.do_turn(self.game)
