from models.error import ResourceNotFound
from models.spotify import SpotifyClient

class Track:
    
    _client = SpotifyClient()

    @classmethod
    def get_top5_tracks_by_artists(cls, artist):
        artist_id = cls._client.get_artist_id(artist)

        if not artist_id:
            raise ResourceNotFound('Cannot find the artist_id of {}'.format(artist))

        return cls._client.get_top_tracks_by_artist_id(artist_id, limit=5)