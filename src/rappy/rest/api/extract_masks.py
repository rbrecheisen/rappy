from flask_restful import Resource


class ExtractMasksResource(Resource):

    URI = '/extract_mask'

    def get(self):
        return 'ExtractMasksResource.get()'
