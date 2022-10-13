from pymongo import MongoClient


class ConnectionMongoDb:
    username = 'admin'
    password = 'aq2D9pbe7BqzoTMk'

    url = f'mongodb+srv://{username}:{password}@cluster0.omd46l0.mongodb.net/?retryWrites=true&w=majority'

    def __init__(self) -> None:
        self._client = MongoClient(self.url)
        self._db = self._client['db']
