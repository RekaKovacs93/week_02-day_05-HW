import unittest
from src.guest import *
from src.song import *
from src.room import *
from src.drink import *

class TestGuest (unittest.TestCase):
    def setUp(self):

        self.song1 = Song("The Doors", "Riders on the storm")
        self.song2 = Song("The Kinks", "Sunny afternoon")
        self.song3 = Song("Velvet Underground", "Venus in furs")

        self.guest1 = Guest("Dave", 100, self.song1)
        self.guest2 = Guest("Kat", 120, self.song2)
        self.guest3 = Guest("Rose", 70, self.song3)  

        self.room1 = Room("one", 0)
        self.room2 = Room("two", 0)
        self.room3 = Room("three", 0)

        

    def test_guest_has_name (self):
        self.assertEqual("Dave", self.guest1.name)

    def test_guest_has_cash(self):
        result = self.guest1.guest_has_cash()
        self.assertEqual(100, result)

    def test_reduce_cash(self):
        self.assertEqual(60, self.guest1.reduce_cash(40))

    def test_guest_loves_song (self):
        self.assertEqual("Whooohoo", self.guest1.guest_loves_song(self.song1))

    def test_guest_loves_song_nope (self):
        self.assertEqual("Nope", self.guest2.guest_loves_song(self.song3))

    



    