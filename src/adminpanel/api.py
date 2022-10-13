from flask import Flask  
from flask_restful import Resource, Api

from adminpanel.lib.utils import deserialize

from adminpanel.lib.perfomance import Perfomance
from adminpanel.lib.info_platform import Platform


class GetPerfomance(Resource):
    def get(self):
        return deserialize(Perfomance().json_perfomance)

class GetPlatform(Resource):
    def get(self):
        return deserialize(Platform().json_platform)


class Run:
    def __init__(self) -> None:
        self._app = Flask(__name__)
        self.api = Api(self._app)
    
    @property
    def app(self):
        return self._app

    @staticmethod
    def main():
        run = Run()
        run.api.add_resource(GetPerfomance, '/perfomance')
        run.api.add_resource(GetPlatform, '/platform')

        run.app.run(debug=True)
