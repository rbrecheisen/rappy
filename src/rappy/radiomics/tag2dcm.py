import os
import binascii
import struct
import pydicom
import numpy as np
from rappy.network import Node


class Tag2Dcm(Node):
    """
    Receives a TomoVision TAG segmentation file and a corresponding DICOM file and
    converts the TAG file to DICOM format.
    """
    def __init__(self):
        super(Tag2Dcm, self).__init__()
        self.add_input('tag_file')
        self.add_input('dcm_file')
        self.add_param('target_dir_path')
        self.add_output('output_file_path')

    @staticmethod
    def _read_tag_file_pixels(f):
        f.seek(0)
        byte = f.read(1)
        # Make sure to check the byte-value in Python 3!!
        while byte != b'':
            byte_hex = binascii.hexlify(byte)
            if byte_hex == b'0c':
                break
            byte = f.read(1)
        values = []
        f.read(1)
        while byte != b'':
            v = struct.unpack('b', byte)
            values.append(v)
            byte = f.read(1)
        values = np.asarray(values)
        values = values.astype(np.uint16)
        return values

    def _build_file_path(self, dcm_file, postfix):
        tag_dcm_file = os.path.splitext(dcm_file.filename)[0]
        tag_dcm_file += postfix
        tag_dcm_file = os.path.join(self.get_param('target_dir_path'), tag_dcm_file)
        return tag_dcm_file

    def _convert_tag_file(self, tag_file, dcm_file, postfix):
        pixels = self._read_tag_file_pixels(tag_file)
        p = pydicom.read_file(dcm_file)
        p.pixel_array.flat = pixels
        p.PixelData = p.pixel_array.tostring()
        os.makedirs(self.get_param('target_dir_path'), exist_ok=True)
        tag_dcm_file = self._build_file_path(dcm_file, postfix)
        p.save_as(tag_dcm_file)
        return tag_dcm_file

    def execute(self):
        self.set_output(
            'output_file_path', self._convert_tag_file(
                self.get_input('tag_file'), self.get_input('dcm_file'), '_tag.dcm'))
