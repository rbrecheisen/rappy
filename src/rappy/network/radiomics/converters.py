import os
from rappy.network.base import Node


class Tag2DICOMConverter(Node):
    """
    This node converts TAG files to DICOM. It expects the following directory structure:

    <root>/
    <root>/subjects/<subject_id>/
    <root>/subjects/<subject_id>/series/<series_id>/
    <root>/subjects/<subject_id>/series/<series_id>/*.dcm
    <root>/subjects/<subject_id>/series/<series_id>/masks/
    <root>/subjects/<subject_id>/series/<series_id>/masks/<mask_id>/
    <root>/subjects/<subject_id>/series/<series_id>/masks/<mask_id>/*.dcm
    """
    def __init__(self):
        super(Tag2DICOMConverter, self).__init__()
        self.add_input('root_dir', data_type='directory')
        self.add_output('output_dir', data_type='directory')

    def execute(self):
        if not self.get_input('root_dir'):
            raise RuntimeError('Input "{}" is mandatory'.format('root_dir'))
        for d in os.listdir(os.path.join(self.get_input('root_dir'), 'subjects')):
            print(d)
