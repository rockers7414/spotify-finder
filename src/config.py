import json

class Config():

    __instance = None

    def __new__(cls, genre_file, credential_file):
        if Config.__instance is None:
            Config.__instance = object.__new__(cls)

        with open(genre_file) as f:
            Config.__instance._genre_dict = json.load(f)

        with open(credential_file) as f:
            Config.__instance._spotify_credential = json.load(f) 

        return Config.__instance

    @classmethod
    def get_instance(cls):
        return cls.__instance

    @property
    def genre_dict(self):
        return self.__instance._genre_dict

    @property
    def spotify_credential(self):
        return (self.__instance._spotify_credential['client_id'],
                self.__instance._spotify_credential['client_secret'])