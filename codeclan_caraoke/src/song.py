class Song:
    def __init__(self, name, artist, genre):
        self.name = name 
        self.artist = artist 
        self.genre = genre 
        self.playlist = []

    def add_song_to_playlist(self, song):
    self.playlist.append(song)