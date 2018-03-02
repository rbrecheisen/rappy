from rappy.network import Node


class Dcm2Masks(Node):
    """
    Receives a DICOM files and outputs N binary masks one for each label (pixel
    value) in the DICOM file.
    """
    def __init__(self):
        super(Dcm2Masks, self).__init__()
        self.add_input('dcm_file')
        self.add_param('labels')
        self.add_output('output_file_paths')

    def execute(self):
        output_file_paths = []
        self.set_output('output_file_paths', output_file_paths)
