import os
from flask import request, current_app, send_from_directory, after_this_request
from flask_restful import Resource
from rappy.radiomics import Dcm2Masks


class Dcm2MasksResourceList(Resource):

    @staticmethod
    def post():

        files = request.files.getlist('files')
        dcm_file = files[0]

        n = Dcm2Masks()
        n.set_input('dcm_file', dcm_file)
        n.set_param('labels', {})
        n.set_param('target_dir_path', os.path.join(current_app.config['UPLOAD_FOLDER'], 'dcm2masks'))
        output_file_paths = n.get_output('output_file_paths')
        output_file_names = []

        for x in output_file_paths:
            output_file_names.append(os.path.split(x)[1])
        return {'output_file_names': output_file_names}


class Dcm2MasksResource(Resource):

    @staticmethod
    def get(file_name):

        output_dir = os.path.join(current_app.config['UPLOAD_FOLDER'], 'dcm2masks')
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
        os.remove(os.path.join(current_app.config['UPLOAD_FOLDER'], 'dcm2masks', file_name))
