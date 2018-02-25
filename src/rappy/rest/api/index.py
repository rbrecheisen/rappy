from flask_restful import Resource


class IndexResource(Resource):

    URI = '/'

    def get(self):
        return 'Hello, world'
