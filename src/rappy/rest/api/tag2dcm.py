from flask_restful import Resource, reqparse
from werkzeug.datastructures import FileStorage


class Tag2DcmResource(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('tag_file', type=FileStorage, location='files')
        parser.add_argument('dcm_file', type=FileStorage, location='files')
        args = parser.parse_args()
        args['tag_file'].save('tag_file.tag')
        args['dcm_file'].save('dcm_file.dcm')
