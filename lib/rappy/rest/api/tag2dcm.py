import os
from flask import request, current_app, send_from_directory, after_this_request
from flask_restful import Resource
from rappy.radiomics import Tag2Dcm


class Tag2DcmResourceList(Resource):
    """
    REST resource that allows calling Tag2Dcm module using uploaded TAG and DICOM
    files. The target directory is set by the resource. The output file ID is
    returned to the client.
    """
    @staticmethod
    def get():
        n = Tag2Dcm()
        return {'info': n.get_info()}

    @staticmethod
    def post():

        files = request.files.getlist('files')
        tag_file = files[0]
        dcm_file = files[1]

        n = Tag2Dcm()
        n.set_input('tag_file', tag_file)
        n.set_input('dcm_file', dcm_file)
        n.set_param('target_dir_path', os.path.join(current_app.config['UPLOAD_FOLDER'], 'tag2dcm'))
        output_file_id = n.get_output('output_file_id')

        return {'output_file_id': output_file_id}


class Tag2DcmResource(Resource):
    """
    REST resource that allows client to retrieve the converted TAG file using the
    output file ID that was returned by the POST.
    """
    @staticmethod
    def get(file_id):

        output_dir = os.path.join(current_app.config['UPLOAD_FOLDER'], 'tag2dcm')
        output_file_id = file_id

        @after_this_request
        # Warning: this may not work on Windows!
        def remove_file(response):
            file_path = os.path.join(output_dir, output_file_id)
            os.remove(file_path)
            return response

        return send_from_directory(output_dir, output_file_id)

    @staticmethod
    def delete(file_id):
        # Can be used to explicitly remove the file if the automatic removal does not work.
        os.remove(os.path.join(current_app.config['UPLOAD_FOLDER'], 'tag2dcm', file_id))
