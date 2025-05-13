import pytest
from lib.song import Song # Make sure 'index.py' contains your Song class

def test_song_count():
    Song.count = 0
    Song.artists = []
    Song.genres = []
    Song.genre_count = {}
    Song.artist_count = {}

    s1 = Song("Hello", "Adele", "Pop")
    s2 = Song("Rolling in the Deep", "Adele", "Pop")
    s3 = Song("99 Problems", "Jay-Z", "Rap")

    assert Song.count == 3
    assert "Adele" in Song.artists
    assert "Jay-Z" in Song.artists
    assert "Pop" in Song.genres
    assert "Rap" in Song.genres
    assert Song.genre_count == {"Pop": 2, "Rap": 1}
    assert Song.artist_count == {"Adele": 2, "Jay-Z": 1}
