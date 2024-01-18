"""
You are part of a team developing a new music streaming app called "MFun." Your task is to design the core functionality that manages the user's music library and playlist creation. Consider the following requirements:

Music library:
Needs to store a collection of songs and their associated metadata (title, artist, album, genre, length).
Must efficiently retrieve songs by various criteria (artist, album, genre, title).
Must prevent duplicate song entries.

Playlists:
Users can create unlimited playlists.
Each playlist can contain any number of songs, but a song cannot be added multiple times to the same playlist.
Songs can be added, removed, or reordered within playlists.
The app should display songs in the order they were added to the playlist.

Which data structure model(s) would you choose to implement the music library and playlist features? Explain your choices, considering the characteristics of each data structure and the specific requirements of the application.

Data structures to consider:
       Tuples, Sets, Lists, Dictionaries, Trees, Graphs, Stacks, Queues

# Prototype code, you can follow different implementation process

class Song:
    def __init__(self, title, artist, album, genre, length):

class MusicLibrary:
    def __init__(self):

    def add_song(self, song):
      
    def get_songs_by_artist(self, artist):

    def get_songs_by_album(self, album):
        
    def get_songs_by_genre(self, genre):
      
    def get_songs_by_title(self, title):

class Playlist:
    def __init__(self, name):

    def add_song(self, song):

    def remove_song(self, song):

    def reorder_songs(self, new_order):

    def display_playlist(self):

# Main Requirement:
# Create song example
# Create a music library
# Add songs to the music library
# Get songs by artist
# Create playlists
# Add songs to playlists
# Display playlists
# Searching for songs by artist

# Sample Output:
Playlist: My Playlist 1
1. Song 1 - Artist 1
2. Song 2 - Artist 2

Songs by Artist 1:
Song 1 - Album 1

"""


class Song:
    def __init__(self, title, artist, album, genre, length):
        self.title = title
        self.artist = artist
        self.album = album
        self.genre = genre
        self.length = length


class MusicLibrary:
    def __init__(self):
        self.songs = {}  # Dictionary to store songs by unique identifier
        # Dictionary to store song IDs by artist for quick retrieval
        self.song_ids_by_artist = {}
        # Dictionary to store song IDs by album for quick retrieval
        self.song_ids_by_album = {}
        # Dictionary to store song IDs by genre for quick retrieval
        self.song_ids_by_genre = {}
        self.unique_song_ids = set()  # Set to prevent duplicate entries

    def add_song(self, song):
        song_id = f"{song.artist}_{song.title}"
        if song_id not in self.unique_song_ids:
            self.songs[song_id] = song
            self.unique_song_ids.add(song_id)

            # Update dictionaries for efficient retrieval
            self.song_ids_by_artist.setdefault(song.artist, set()).add(song_id)
            self.song_ids_by_album.setdefault(song.album, set()).add(song_id)
            self.song_ids_by_genre.setdefault(song.genre, set()).add(song_id)

            return True  # Song added successfully
        else:
            return False  # Song already exists in the library

    def get_songs_by_artist(self, artist):
        return [self.songs[song_id] for song_id in self.song_ids_by_artist.get(artist, set())]

    def get_songs_by_album(self, album):
        return [self.songs[song_id] for song_id in self.song_ids_by_album.get(album, set())]

    def get_songs_by_genre(self, genre):
        return [self.songs[song_id] for song_id in self.song_ids_by_genre.get(genre, set())]

    def get_songs_by_title(self, title):
        # Since titles are unique, we can directly access the song
        song_id = f"{title}_{title}"
        return [self.songs.get(song_id)]


class Playlist:
    def __init__(self, name):
        self.name = name
        self.song_ids = []  # List to maintain order of songs in the playlist
        self.unique_song_ids = set()  # Set to prevent duplicate entries in the playlist

    def add_song(self, song):
        if song and song.title not in self.unique_song_ids:
            self.song_ids.append(song.title)
            self.unique_song_ids.add(song.title)
            return True  # Song added to the playlist successfully
        else:
            return False  # Song is either None or already in the playlist

    def remove_song(self, title):
        if title in self.unique_song_ids:
            self.song_ids.remove(title)
            self.unique_song_ids.remove(title)
            return True  # Song removed from the playlist successfully
        else:
            return False  # Song not in the playlist

    def reorder_songs(self, new_order):
        # Assuming new_order is a list of song titles
        self.song_ids = [
            title for title in new_order if title in self.unique_song_ids]

    def display_playlist(self):
        print(f"Playlist: {self.name}")
        for index, title in enumerate(self.song_ids, start=1):
            print(f"{index}. {title}")


if __name__ == "__main__":
    song1 = Song("Song 1", "Artist 1", "Album 1", "Genre 1", "3:30")
    song2 = Song("Song 2", "Artist 2", "Album 2", "Genre 2", "4:15")

    music_library = MusicLibrary()
    music_library.add_song(song1)
    music_library.add_song(song2)

    playlist1 = Playlist("My Playlist 1")
    playlist1.add_song(song1)
    playlist1.add_song(song2)

    playlist1.display_playlist()

    songs_by_artist1 = music_library.get_songs_by_artist("Artist 1")
    print(f"Songs by Artist 1:")
    for song in songs_by_artist1:
        print(f"{song.title} - {song.album}")
