import unittest 
from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Gimmie Shelter", "Rolling Stones", "Rock")

    def test_track_has_title(self):
        self.assertEqual("Gimmie Shelter", self.song_1.title)

    def test_track_has_artist(self):
        self.assertEqual("Rolling Stones", self.song_1.artist)

    def test_track_has_genre(self):
        self.assertEqual("Rock", self.song_1.genre)

    def test_song_can_be_added_to_playlist(self)