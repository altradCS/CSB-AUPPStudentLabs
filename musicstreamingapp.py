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
d
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
        self.songs = {}  # dictionary to store songs by unique identifier
        # dictionary to store song ids by artist for quick retrieval
        self.song_ids_by_artist = {}
        self.song_ids_by_album = {}
        self.song_ids_by_genre = {}
        self.unique_song_ids = set()  # set to prevent duplicate song entries

    def add_song(self, song):
        song_id = f"{song.artist}_{song.title}"
        if song_id not in self.unique_song_ids:
            self.songs[song_id] = song
            self.unique_song_ids.add(song_id)

            # update dictionaries for quick retrieval
            self.song_ids_by_artist.setdefault(song.artist, set()).add(song_id)
            self.song_ids_by_album.setdefault(song.album, set()).add(song_id)
            self.song_ids_by_genre.setdefault(song.genre, set()).add(song_id)

            return True  # song added successfully
        else:
            return False  # song already exists in the library

    def get_songs_by_artist(self, artist):
        return [self.songs[song_id] for song_id in self.song_ids_by_artist.get(artist, set())]

    def get_songs_by_album(self, album):
        return [self.songs[song_id] for song_id in self.song_ids_by_album.get(album, set())]

    def get_songs_by_genre(self, genre):
        return [self.songs[song_id] for song_id in self.song_ids_by_genre.get(genre, set())]

    def get_songs_by_title(self, title):
        song_id = f"{title}_{title}"
        return [self.songs.get(song_id)]


class Playlist:
    def __init__(self, name):
        self.name = name
        self.song_ids = []    # list to maintain order of songs in the playlist
        self.unique_song_ids = set()  # set to prevent duplicate song entries in the playlist

    def add_song(self, song):
        if song and song.title not in self.unique_song_ids:
            self.song_ids.append(song.title)
            self.unique_song_ids.add(song.title)
            return True   # song added successfully to the playlist
        else:
            return False   # song is either None or already in the playlist

    def remove_song(self, title):
        if title in self.unique_song_ids:
            self.song_ids.remove(title)
            self.unique_song_ids.remove(title)
            return True   # song removed successfully from the playlist
        else:
            return False   # song is not in the playlist

    def reorder_songs(self, new_order):
        self.song_ids = [
            title for title in new_order if title in self.unique_song_ids]

    def display_playlist(self):
        print(f"Playlist: {self.name}")
        for index, title in enumerate(self.song_ids, start=1):
            print(f"{index}. {title}")


if __name__ == "__main__":
    # Create song example
    song1 = Song("Song 1", "Artist 1", "Album 1", "Genre 1", 2.5)
    song2 = Song("Song 2", "Artist 2", "Album 2", "Genre 2", 3.5)
    song3 = Song("Song 3", "Artist 3", "Album 3", "Genre 3", 4.5)
    song4 = Song("Song 4", "Artist 4", "Album 4", "Genre 4", 5.5)
    song5 = Song("Song 5", "Artist 5", "Album 5", "Genre 5", 6.5)

    music_library = MusicLibrary()
    music_library.add_song(song1)
    music_library.add_song(song2)
    music_library.add_song(song3)
    music_library.add_song(song4)
    music_library.add_song(song5)

    Playlist1 = Playlist("My Playlist 1")
    Playlist1.add_song(song1)
    Playlist1.add_song(song2)
    Playlist1.add_song(song3)
    Playlist2 = Playlist("My Playlist 2")
    Playlist2.add_song(song4)
    Playlist2.add_song(song5)

    Playlist1.add_song(song1)  # try to add song1 again to Playlist1
    Playlist1.remove_song(song3.title)  # remove song3 from Playlist1
    Playlist1.display_playlist()
    Playlist2.display_playlist()

    # reorder songs in Playlist1
    Playlist1.reorder_songs([song2.title, song1.title])
    Playlist1.display_playlist()

    songs_by_artist1 = music_library.get_songs_by_artist("Artist 1")
    songs_by_artist2 = music_library.get_songs_by_artist("Artist 2")

    print(f"Songs by Artist 1:")
    for song in songs_by_artist1:
        print(f"{song.title} - {song.album} - {song.genre} - length: {song.length}")
    print(f"Songs by Artist 2:")
    for song in songs_by_artist2:
        print(f"{song.title} - {song.album} - {song.genre} - length: {song.length}")
