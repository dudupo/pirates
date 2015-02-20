import engine 
from vector import Vector
from pirate import Pirate
class Game:
    MAX_AMOUNT_OF_PIRATES=6;
    direaction = {
        "0"  :    Vector(0,0 ) ,
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
        return  [i for i in self.player._pirates if i in engine.living_pirates]
    def get_my_dead_pirates(self):
        'returns a list with all dead pirates'
        return [i for i in self.player._pirates if i in engine.dead_pirates]
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
        return [i for i in engine.islands if i.get_owner() == self.player]
    def get_not_my_islands(self):
        'returns all of the islands that do not belong to this players'
        return [i for i in engine.islands if i.get_owner() != self.player]
    def get_enemy_islands(self):
        return [i for i in engine.islands if (i.get_owner() != self.player) and (i.get_owner() != None) ]

    def set_sail(self,pirate,direaction):
        
        if not isinstance(direaction , list):
            direaction = [direaction]

        for dire in direaction:
            for p in engine.pirates:
                if p.uniq != pirate.uniq :
                    p_next_location = p.location + Game.direaction[p.current_direaction]
                    if pirate.location+Game.direaction[dire] == p_next_location:
                        direaction.remove(dire)
                        break

            
        if len(direaction) > 0 :
            direaction = direaction[0]
            pirate.current_direaction = direaction
            direaction=Game.direaction[direaction]
            engine.tasks.append(('MOVE',pirate,direaction))
            return True
        else :
            return False 
        



    def get_directions(self,obja,objb):
        toret=list()
        
        num_of_south =  obja.location.y - objb.location.y 
        num_of_north =  objb.location.y - obja.location.y 
        num_of_east  =  objb.location.x - obja.location.x 
        num_of_weast =  obja.location.x - objb.location.x 

        if num_of_south > 0 :
            toret += (['s'] * num_of_south)
        if num_of_weast > 0:
            toret += (['w'] * num_of_weast)
        if num_of_north > 0:
            toret += (['n'] * num_of_north)
        if num_of_east > 0 :
            toret += (['e'] * num_of_east) 

        '''
        for dire in toret:
            for p in engine.pirates:
                if p.uniq != obja.uniq :
                    p_next_location = p.location + Game.direaction[p.current_direaction]
                    if obja.location+Game.direaction[dire]== p_next_location:
                        toret.remove(dire)
                        break 

        if isinstance(obja ,Pirate) and len(toret) > 0:
            obja.current_direaction = toret[0]
        '''

        return toret
