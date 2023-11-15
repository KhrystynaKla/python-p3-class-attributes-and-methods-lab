class Song:
    genres=[]
    artists=[]
    artist_count={}
    count=0
    genre_count={}
    def __init__(self, name, artist, genre):
        self.name=name
        self.artist=artist
        self.genre=genre
        Song.add_count()
        Song.add_genre(self.genre)
        Song.add_to_artists(self.artist)
        
    @classmethod
    def add_count(cls):
        cls.count+=1
    
    @classmethod
    def add_genre(cls, genre):
        if genre not in Song.genres:
            Song.genres.append(genre)
        if (genre not in Song.genre_count.keys()):
            Song.genre_count[genre]=1
        else:
            Song.genre_count[genre]+=1
    
    @classmethod
    def add_to_artists(cls, artist):
        if artist not in Song.artists:
            Song.artists.append(artist)
        if (artist not in Song.artist_count.keys()):
            Song.artist_count[artist]=1
        else:
            Song.artist_count[artist]+=1