class Game:
    'each player has his own "game" instanse' 
    def __init__(self,enigne,player):
        ''' * engine is the phsical world that stores all the ships and islands.
            * player is the instanse that this game belongs to.'''
        pass
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