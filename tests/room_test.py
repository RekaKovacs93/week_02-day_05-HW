import unittest
from src.guest import *
from src.song import *
from src.room import *
from src.drink import *

class TestRoom (unittest.TestCase):
    def setUp(self):

        self.room1 = Room("one", 0)
        self.room2 = Room("two", 0)
        self.room3 = Room("three", 0)

        self.song1 = Song("The Doors", "Riders on the storm")
        self.song2 = Song("The Kinks", "Sunny afternoon")
        self.song3 = Song("Velvet Underground", "Venus in furs")

        self.guest1 = Guest("Dave", 100, self.song1)
        self.guest2 = Guest("Kat", 120, self.song2)
        self.guest3 = Guest("Rose", 70, self.song3)

        self.drink1 = Drink("Corona", 2)


        

    def test_room_has_name(self):
        self.assertEqual("one", self.room1.name)


    def test_number_of_guests(self):
        self.assertEqual(0, self.room1.number_of_guests())


    def test_add_guest(self):
        self.room1.add_guest(self.guest1)
        self.guest1.reduce_cash(self.room1.fee)
        self.assertEqual(10, self.room1.total_cash)
        self.assertEqual(90, self.guest1.cash)
        self.assertEqual(1, self.room1.number_of_guests())


    def test_sell_drink (self):
        self.guest3.reduce_cash(self.drink1.price)
        self.room1.sell_drink(self.drink1.price)
        self.assertEqual(68, self.guest3.cash)
        self.assertEqual(2, self.room1.total_cash)


    @unittest.skip("delete this line to run the test")
    def test_add_guest(self):
        self.room1.add_guest(self.guest1)
        self.assertEqual("Sorry, room is full", self.room1.add_guest(self.guest1))


    def test_add_song(self):
        self.room3.add_song(self.song3)
        self.assertEqual(1, self.room3.number_of_songs())

    

        