import requests
from config import Config

class SpotifyClient:

    class SpotifyClientError(Exception):
        pass

    __instance = None

    def __new__(cls):
        if SpotifyClient.__instance is None:
            SpotifyClient.__instance = object.__new__(cls)

            # get the token
            resp = requests.post('https://accounts.spotify.com/api/token',
                                 data={'grant_type': 'client_credentials'},
                                 auth=Config.get_instance().spotify_credential)
            
            if resp.status_code == 200:
                body = resp.json()
                SpotifyClient.__instance._token = body['access_token']
            else:
                raise SpotifyClient.SpotifyClientError('Failed to auth')

        return SpotifyClient.__instance

    def __get_headers(self):
        return {
            'Authorization': 'Bearer {}'.format(self._token)
        }

    def get_artist_id(self, name):
        headers = self.__get_headers()
        params = {
            'q': name,
            'type': 'artist'
        }
        resp = requests.get('https://api.spotify.com/v1/search', params=params, headers=headers)

        if resp.status_code == 200:
            body = resp.json()
            if body['artists']['total'] > 0:
                return body['artists']['items'][0]['id']
        else:
            raise SpotifyClient.SpotifyClientError('Failed to fetch artist info')

    def get_top_tracks_by_artist_id(self, artist_id, limit=None):
        headers = self.__get_headers()
        params = {
            'country': 'TW'
        }
        resp = requests.get('https://api.spotify.com/v1/artists/{}/top-tracks'.format(artist_id), params=params, headers=headers)

        if resp.status_code == 200:
            body = resp.json()
            return body['tracks'][:5]
        else:
            raise SpotifyClient.SpotifyClientError('Failed to fetch popular track by artist id')