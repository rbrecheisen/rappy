import os
from flask import request, current_app, send_from_directory, after_this_request
from flask_restful import Resource
from rappy.radiomics import Tag2Dcm


class Tag2DcmResourceList(Resource):

    @staticmethod
    def post():

        files = request.files.getlist('files')
        tag_file = files[0]
        dcm_file = files[1]

        n = Tag2Dcm()
        n.set_input('tag_file', tag_file)
        n.set_input('dcm_file', dcm_file)
        n.set_param('target_dir_path', os.path.join(current_app.config['UPLOAD_FOLDER'], 'tag2dcm'))
        output_file_path = n.get_output('output_file_path')

        output_file_name = os.path.split(output_file_path)[1]
        return {'output_file_name': output_file_name}


class Tag2DcmResource(Resource):

    @staticmethod
    def get(file_name):

        output_dir = os.path.join(current_app.config['UPLOAD_FOLDER'], 'tag2dcm')
        output_file_name = file_name

        @after_this_request
        # Warning: this may not work on Windows!
        def remove_file(response):
            file_path = os.path.join(output_dir, output_file_name)
            os.remove(file_path)
            return response

        return send_from_directory(output_dir, output_file_name)

    @staticmethod
    def delete(file_name):
        os.remove(os.path.join(current_app.config['UPLOAD_FOLDER'], 'tag2dcm', file_name))
