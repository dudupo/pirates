
import importlib
import emulator
class _do_turn:
	def __init__(self, name_of_bot):	
		importlib.import_module(name_of_bot)
		self.do_turn = name_of_bot.do_turn

	def __call__():
		self.do_turn()
		emulator.update()