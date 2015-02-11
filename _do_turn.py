
from importlib import import_module

DO_TURN_METHOD_NAME= 'do_turn'
class _do_turn:
	'A class that represents the function "do_turn" in each bot'
	def __init__(self, name_of_bot ,game):
		mod = import_module(name_of_bot)
		self.do_turn = getattr(mod ,DO_TURN_METHOD_NAME)
	def __call__():
		self.do_turn()
