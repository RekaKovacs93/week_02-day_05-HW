class Room:
    def __init__(self, name, total_cash):
        self.total_cash = total_cash
        self.fee = 10
        self.name = name
        self.guests = []
        self.songs = []

    def number_of_guests(self):
        return len(self.guests)
    
    def sell_drink(self, num):
        self.total_cash += num
    
    def add_guest(self, guest):
        if len(self.guests) < 5:
            self.guests.append(guest)
            self.total_cash += self.fee
        else:
            return "Sorry, room is full"
        
    def number_of_songs(self):
        return len(self.songs)
    
    def add_song(self, song):
        self.songs.append(song)
    
    def remove_song(self,song):
        self.songs.remove(song)
    
        