import os
import unittest
from rappy.network.radiomics.loaders import ImageDataLoader


class LoadImageDataTest(unittest.TestCase):

    def makedirs(self, dir_path):
        os.makedirs(dir_path, exist_ok=True)

    def setUp(self):
        d = '/tmp/rappy/load_image_data/patients/pat_0001/modalities/mod_0001/studies/stu_0001/series/ser_0001'
        self.makedirs(d)

    @staticmethod
    def test_execute_validates_directories():
        node = ImageDataLoader()
        node.set_input('root_dir', '/Volumes/USB_SECURE1/Data/BodyComposition/AkenMaastricht')
        node.execute()
        d = node.get_output('subjects')
        raise RuntimeError('I was here... ')
