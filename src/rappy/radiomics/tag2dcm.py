import os
import binascii
import struct
import pydicom
import numpy as np
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

    @staticmethod
    def _build_file_path(tag_file, dcm_file, postfix):
        dcm_dir = os.path.split(dcm_file)[0]
        tag_base = os.path.splitext(tag_file)[0]
        tag_dcm_file = os.path.join(dcm_dir, tag_base + postfix)
        return tag_dcm_file

    def _convert_tag_file(self, tag_file, dcm_file, postfix):
        pixels = self._read_tag_file_pixels(tag_file)
        p = pydicom.read_file(dcm_file)
        p.pixel_array.flat = pixels
        p.PixelData = p.pixel_array.tostring()
        tag_dcm_file = self._build_file_path(tag_file, dcm_file, postfix)
        p.save_as(tag_dcm_file)
        return tag_dcm_file

    def execute(self):
        self.set_output(
            'tag_dcm_file', self._convert_tag_file(
                self.get_input('tag_file'), self.get_input('dcm_file'), '_tag.dcm'))
