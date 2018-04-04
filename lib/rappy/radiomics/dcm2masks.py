import os
import pydicom
import numpy as np
from rappy.network import Node


class Dcm2Masks(Node):
    """
    Receives a DICOM files and outputs N binary masks one for each label (pixel
    value) in the DICOM file.
    """
    def __init__(self):

        super(Dcm2Masks, self).__init__()

        self.add_input('dcm_file', data_type='string')
        self.add_param('label_map', data_type='string')
        self.add_param('out_dir', data_type='string')
        self.add_output('out_files', data_type='string')

    @staticmethod
    def _create_mask(pixels, label):
        print('Dcm2Masks._create_mask() creating mask for label {}'.format(label))
        pixels_copy = np.copy(pixels)
        pixels_copy[pixels_copy != label] = np.uint16(0)
        pixels_copy[pixels_copy == label] = np.uint16(1)
        return pixels_copy

    @staticmethod
    def _update_p(p, pixels):
        print('Dcm2Masks._update_p() updating DICOM attributes')
        # TODO: Make these into parameters
        p.PixelRepresentation = 0
        p.BitsAllocated = 16
        p.BitsStored = 12
        p.HighBit = 11
        p.RescaleIntercept = 0
        p.RescaleSlope = 1
        p.PixelData = pixels.tostring()
        return p

    def _extract_binary_masks(self, file_path, label_map, out_dir):
        print('Dcm2Masks._extract_binary_masks() {}'.format(file_path))
        print('Dcm2Masks._extract_binary_masks() label map: {}'.format(label_map))
        print('Dcm2Masks._extract_binary_masks() reading DICOM')
        p = pydicom.read_file(open(file_path, 'rb'))
        pixels = p.pixel_array.flat
        labels = np.unique(pixels).tolist()
        masks = {}
        out_files = []
        print('Dcm2Masks._extract_binary_masks() creating masks')
        for label in labels:
            if str(label) not in label_map:
                continue
            # For each label extract pixels and set them 0/1
            pixels_copy = self._create_mask(pixels, label)
            p = self._update_p(p, pixels_copy)
            # Extract separate file name from DICOM file path
            file_name = os.path.split(file_path)[1]  # e.g., S_934779987_tag.dcm
            file_base, file_ext = os.path.splitext(file_name)[0], os.path.splitext(file_name)[1]
            out_file_name = file_base + '_' + label_map[str(label)] + file_ext
            out_file_path = os.path.join(out_dir, out_file_name)
            p.save_as(out_file_path)
            out_files.append(out_file_path)
        return out_files

    def execute(self):
        print('Dcm2Masks.execute()')
        dcm_file = self.get_input('dcm_file')
        os.makedirs(self.get_param('out_dir'), exist_ok=True)
        out_files = self._extract_binary_masks(
            dcm_file, self.get_param('label_map'), self.get_param('out_dir'))
        self.set_output('out_files', out_files)
