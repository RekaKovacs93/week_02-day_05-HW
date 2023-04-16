class Guest:
    def __init__(self, name, cash, fav_song):
        self.name = name
        self.cash = cash
        self.fav_song = fav_song

    def guest_has_name(self):
        return self.name
    
    def guest_has_cash(self):
        return self.cash
    
    def reduce_cash(self, num):
        self.cash -= num
        return self.cash
    
    def guest_loves_song(self, song):
        if self.fav_song == song:
            return "Whooohoo"
        return "Nope"
    