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
    <root>/subjects/<subject_id>/modalities/<modality_id>/studies/<study_id>/series/<series_id>/*.dcm
    <root>/subjects/<subject_id>/modalities/<modality_id>/studies/<study_id>/series/<series_id>/masks
    <root>/subjects/<subject_id>/modalities/<modality_id>/studies/<study_id>/series/<series_id>/masks/<mask_id>
    <root>/subjects/<subject_id>/modalities/<modality_id>/studies/<study_id>/series/<series_id>/masks/<mask_id>/*.dcm
    
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

    Question is how do we setup this node in RapidMiner? It would be nice if the operator had a "Select directory"
    button or we can use another operator in RapidMiner to select a directory and pass the string to ImageDataLoader.
    """

    def __init__(self):
        super(ImageDataLoader, self).__init__()
        self.add_input('root_dir', data_type='directory')
        self.data = {}

    def execute(self):
        if not self.get_input('root_dir'):
            raise RuntimeError('Input "{}" is mandatory'.format('root_dir'))

    def get_subjects(self, path=True):
        return []

    def get_modalities(self, path=True, subject=None):
        return []

    def get_studies(self, path=True, subject=None, modality=None):
        return []

    def get_series(self, path=True, subject=None, modality=None, study=None):
        return []

    def get_masks(self, path=True, subject=None, modality=None, study=None, series=None):
        return []
