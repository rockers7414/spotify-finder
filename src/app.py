from config import Config
# Initialize configuration
Config(genre_file='src/genres.json', credential_file='src/credential.json')

from controllers.track import TrackGenreList
from flask import Flask
from flask_restful import Api


app = Flask(__name__)
api = Api(app)

api.add_resource(TrackGenreList, '/tracks/<string:genre>')

if __name__ == '__main__':
    app.run()