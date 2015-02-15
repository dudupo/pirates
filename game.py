import engine 
from vector import Vector
class Game:
    MAX_AMOUNT_OF_PIRATES=6;
    direaction = {
        "e"  :    Vector(1, 0) , 
        "w"  :    Vector(-1,0),
        "n"  :    Vector(0 ,1),
        "s"  :    Vector(0,-1)   }

    'each player has his own "game" instanse' 
    def __init__(self ,player):
        ''' * engine is the phsical world that stores all the ships and islands.
            * player is the instanse that this game belongs to.'''
        self.player = player

    def get_my_pirates(self):
        'returns all of the pirates belonging to that player '
        return self.player._pirates
    def get_my_dead_pirates(self):
        'returns a list with all dead pirates'
        daed=list()
        pirates = self.player._pirates
        for pirate in pirates:
            if not pirate.alive:
                dead.append(pirate)
        return dead
    def get_enemy_pirates(self):
        'returns all the enemy pirates'
        enemy= list()
        for player in engine.players:
            if player != self.player:
                enemy+=player._pirates
        return enemy
    def get_islands(self):
        'returns all islands'
        return engine.islands
    def get_my_islands(self):
        'returns all of the islands that belong to this player'
        toret=list()
        for island in engine.islands:
            if islands.get_owner() == self.player:
                toret.append(island)
        return toret
    def get_not_my_islands(self):
        'returns all of the islands that do not belong to this players'
        toret=list()
        for island in engine.islands:
            if islands.get_owner() != self.player:
                toret.append(island)
        return toret
    def set_sail(self,pirate,direaction):
        if not isinstance(direaction, Vector):
            direaction=Game.direaction[direaction]
        engine.tasks.append(('MOVE',pirate,direaction))
        

        
    

