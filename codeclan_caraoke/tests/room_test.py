import unittest 
from src.room import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room("Rock Room", self.song_1.title)

    def test_room_has_name(self):
        self.assertEqual("Rock Room")