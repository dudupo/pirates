import engine 

class Game:
    direaction = {
        "e"  :     1 , 
        "w"  :    -1 ,
        "n"  :    1j ,
        "s"  :   -1j    }

    'each player has his own "game" instanse' 
    def __init__(self ,player):
        ''' * engine is the phsical world that stores all the ships and islands.
            * player is the instanse that this game belongs to.'''
        self.player = player
    def get_my_pirates(self):
        'returns all of the pirates belonging to that player '
    def get_enemy_pirates(self):
        'returns all the enemy pirates'
    def get_islands(self):
        'returns all islands'
    def get_my_islands(self):
        'returns all of the islands that belong to this player'
    def get_not_my_islands(self):
        'returns all of the islands that do not belong to this players'
   

    def SetSail(self , pirate , Direaction):
        for direact in Direaction:
            pirate.power -= 1
            pirate.location += Game.direaction[direact]

            Task = engine._task(engine.updateLists , [pirate])
            engine.push_Task(Task ,self.player)

            if pirate.power == 0:
                break 
    

