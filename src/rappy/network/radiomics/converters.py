import os
from rappy.network.base import Node


class Tag2DICOMConverter(Node):
    """
    This node converts a single TAG file (and corresponding parent DICOM) to DICOM. It expects
    the TAG and parent DICOM file to have the same name.
    """
    def __init__(self):

        super(Tag2DICOMConverter, self).__init__()

        self.add_input('parent_dicom_file', data_type='file')
        self.add_input('tag_file', data_type='file')
        self.add_input('label_map', data_type='dict')
        self.add_param('output_dir', data_type='dir')
        self.add_output('output_dir', data_type='dir')

    def execute(self):

        # Validate inputs
        if not self.get_input('parent_dicom_file'):
            raise RuntimeError('Input "{}" is mandatory'.format('parent_dicom_file'))
        if not self.get_input('tag_file'):
            raise RuntimeError('Input "{}" is mandatory'.format('tag_file'))

        # Create output directory based on parameter
        os.makedirs(self.get_param('output_dir'), exist_ok=True)
        # Write some content into the directory
        with open(os.path.join(self.get_param('output_dir'), 'file.txt'), 'w') as f:
            f.write('Hello, world!\n')
        # Set output directory as the output of the node
        self.set_output('output_dir', self.get_param('output_dir'))
