import os
import unittest
from rappy.network.radiomics.loaders import ImageDataLoader
from rappy.network.radiomics.converters import Tag2DICOMConverter


class NodeTest(unittest.TestCase):

    @staticmethod
    def test_tag2dicom_converter():
        node = Tag2DICOMConverter()
        node.set_input('root_dir', '/Volumes/USB_SECURE1/Data/BodyComposition/AkenMaastricht')
        node.execute()

