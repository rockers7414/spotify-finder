import random
from config import Config
from flask_restful import Resource, abort
from models.track import Track
from models.error import ResourceNotFound, InvalidArgument


class TrackGenreList(Resource):

    genre_dict = Config.get_instance().genre_dict

    def get(self, genre):
        try:
            if genre not in self.genre_dict:
                raise InvalidArgument('Invalid genre')

            artists = self.genre_dict[genre]
            selected = random.randrange(0, len(artists))
            return Track.get_top5_tracks_by_artists(artists[selected])
        except InvalidArgument as e:
            abort(400, message=str(e))
        except ResourceNotFound as e:
            abort(404, message='Resource Not Found')
        except e:
            abort(500, message='Unknown Error')
