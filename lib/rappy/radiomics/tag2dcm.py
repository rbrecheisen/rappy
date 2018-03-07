import os
import shutil
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

        self.add_input('tag_file', data_type='string')
        self.add_input('dcm_file', data_type='string')
        self.add_param('output_dir', data_type='string')
        self.add_output('output_file', data_type='string')
        self.add_param('overwrite', data_type='boolean', default=False)

    @staticmethod
    def _read_tag_file_pixels(f):

        print('Tag2Dcm._read_tag_file_pixels() {}'.format(f))
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

    def _build_output_file_path(self, tag_file):

        output_file = os.path.split(tag_file)[1]
        output_file = os.path.splitext(output_file)[0]
        output_file = output_file + '_tag.dcm'
        output_file = os.path.join(self.get_param('output_dir'), output_file)
        print('Tag2Dcm._build_file_path() output_file = {}'.format(output_file))

        return output_file

    def _convert_tag_file(self, tag_file, dcm_file):

        print('Tag2Dcm._convert_tag_file() {}/{}'.format(tag_file, dcm_file))
        print('Tag2Dcm._convert_tag_file() reading TAG file pixels')
        pixels = self._read_tag_file_pixels(open(tag_file, 'rb'))

        print('Tag2Dcm._convert_tag_file() reading DICOM')
        p = pydicom.read_file(open(dcm_file, 'rb'))

        print('Tag2Dcm._convert_tag_file() replacing pixels in DICOM copy')
        p.pixel_array.flat = pixels
        p.PixelData = p.pixel_array.tostring()

        if self.get_param('overwrite'):
            print('Tag2Dcm._convert_tag_file() removing output_dir')
            shutil.rmtree(self.get_param('output_dir'), ignore_errors=True)

        print('Tag2Dcm._convert_tag_file() creating output_dir')
        os.makedirs(self.get_param('output_dir'), exist_ok=True)

        print('Tag2Dcm._convert_tag_file() building output_file path')
        output_file = self._build_output_file_path(tag_file)

        print('Tag2Dcm._convert_tag_file() saving output_file')
        p.save_as(output_file)

        print('Tag2Dcm._convert_tag_file() done')
        return output_file

    def execute(self):

        print('Tag2Dcm.execute()')
        self.set_output(
            'output_file', self._convert_tag_file(
                self.get_input('tag_file'), self.get_input('dcm_file')))
