from flask import request
from flask_restful import Resource
from rappy.radiomics import Tag2Dcm


class Tag2DcmResource(Resource):

    URI = '/tag2dcm'

    def post(self):
        files = request.files.getlist('files')
        tag_file = files[0]
        dcm_file = files[1]
        n = Tag2Dcm()
        print(n.get_info())
        # n.set_input('tag_file', tag_file)
        # n.set_input('dcm_file', dcm_file)
        # tag_dcm_file = n.get_output('tag_dcm_file')
        # print(tag_dcm_file)
