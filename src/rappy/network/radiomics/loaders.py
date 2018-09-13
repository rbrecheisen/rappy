import os
from rappy.network.base import Node


class ImageDataLoader(Node):

    """ This node is responsible for loading imaging data. The image data is loaded from hard disk and
    must be organized in the following hierarchy:

    <root>
    <root>/subjects
    <root>/subjects/<subject_id>
    <root>/subjects/<subject_id>/modalities
    <root>/subjects/<subject_id>/modalities/<modality_id>
    <root>/subjects/<subject_id>/modalities/<modality_id>/studies
    <root>/subjects/<subject_id>/modalities/<modality_id>/studies/<study_id>
    <root>/subjects/<subject_id>/modalities/<modality_id>/studies/<study_id>/series
    <root>/subjects/<subject_id>/modalities/<modality_id>/studies/<study_id>/series/<series_id>
    <root>/subjects/<subject_id>/modalities/<modality_id>/studies/<study_id>/series/<series_id>/objects
    <root>/subjects/<subject_id>/modalities/<modality_id>/studies/<study_id>/series/<series_id>/objects/<object_id>
    
    This hierarchy supports a wide variety of modalities and scan types. For example, fMRI scans result in a single
    series that consists of multiple volumes acquired over time. Each volume in this case would be an object. If the
    object is DICOM, it contains multiple slices. If it is NIFTI, it will contain a single file.
    
    Loading image data will build up an internal dictionary that can be traversed in a similar manner as the
    directories. Extra convenience methods allow retrieval of full path information for different objects. For
    example,
    
    get_subjects()
    get_modalities(subject=None)
    get_studies(subject=None, modality=None)
    get_series(subject=None, modality=None, study=None)
    get_objects(subject=None, modality=None, study=None)

    Based on different combinations of the parameters you get different lists. For example,
    get_studies(subject='x', modality='y') returns a list of study IDs for subject 'x' and modality 'y'. However, if
    you call get_studies(modality='y') you get a list of all modalities regardless of subject.
    """

    def __init__(self):
        super(ImageDataLoader, self).__init__()
        self.add_input('root_dir', data_type='directory')
        self.add_output('subjects', data_type='list')
        self.add_output('modalities', data_type='list')
        self.add_output('studies', data_type='list')
        self.add_output('series', data_type='list')
        self.add_output('objects', data_type='list')
        self.add_param('path', data_type='bool', default=True)
        self.add_param('select_subject', data_type='string', default=None)
        self.add_param('select_modality', data_type='string', default=None)
        self.add_param('select_study', data_type='string', default=None)
        self.add_param('select_series', data_type='string', default=None)
        self.data = {}

    def execute(self):

        # STEP 0: Validate input and parameters
        if not self.get_input('root_dir'):
            raise RuntimeError('Input "{}" is mandatory'.format('root_dir'))

        # STEP 1: Validate the directory structure
        for root, dirs, files in os.walk(self.get_input('root_dir')):
            for f in files:
                print(f)

        # STEP 2: Build dictionary
        pass

    def get_subjects(self):
        return []

    def get_modalities(self):
        return []

    def get_studies(self):
        return []

    def get_series(self):
        return []

    def get_objects(self):
        return []
