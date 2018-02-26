from rappy.network import Node


class Tag2Dcm(Node):

    def __init__(self):
        super(Tag2Dcm, self).__init__()
        self.add_input(
            name='tag_file',
            desc='TAG file to be converted and containing the mask annotations')
        self.add_input(
            name='dcm_file',
            desc='DICOM file containing original image')
        self.add_output(
            name='tag_dcm_file',
            desc='Converted TAG file in DICOM format')

    def execute(self):
        self.set_output('tag_dcm_file', 'bla')
