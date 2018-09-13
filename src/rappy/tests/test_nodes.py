import os
import unittest
from rappy.network.radiomics.converters import Tag2DICOMConverter


class NodeTest(unittest.TestCase):

    @staticmethod
    def test_tag2dicom_converter():

        node = Tag2DICOMConverter()
        node.set_input('parent_dicom_file', '/Users/Ralph/Data/RappyTest/image.dcm')
        node.set_input('tag_file', '/Users/Ralph/Data/RappyTest/image.tag')
        node.set_input('label_map', {'1': 'muscle', '5': 'SAT', '7': 'VAT'})
        node.set_param('output_dir', './output')
        node.execute()

        for f in os.listdir(node.get_output('output_dir')):
            print(f)
