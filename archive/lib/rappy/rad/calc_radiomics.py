import os
import pydicom
import SimpleITK
from radiomics import featureextractor
from rappy.network import Node


class CalculateRadiomicsFeatures(Node):
    """
    Calculates radiomics features for a given DICOM file and corresponding mask. Features
    are calculated based on PyRadiomics. The output file is list of name/value pairs.
    """
    def __init__(self):

        super(CalculateRadiomicsFeatures, self).__init__()

        self.add_input('in_file', data_type='string')
        self.add_input('mask_file', data_type='string')
        self.add_param('out_dir', data_type='string')
        self.add_param('settings', data_type='dict', default={
            'binWidth': 5, 'resampledPixelSpacing': None, 'interpolator': SimpleITK.sitkBSpline,
        })
        self.add_output('out_file', data_type='string')

    @staticmethod
    def _get_slope_and_intercept(image):
        print('CalculateRadiomicsFeatures._get_slope_and_intercept()')
        p = pydicom.read_file(image)
        return p.RescaleSlope, p.RescaleIntercept

    def _load_image_and_mask(self, i, m):
        print('CalculateRadiomicsFeatures._load_image_and_mask()')
        slope, intercept = self._get_slope_and_intercept(i)
        image = SimpleITK.ReadImage(i)
        image = slope * image + intercept
        mask = SimpleITK.ReadImage(m)
        return image, mask

    def _extract_features(self, image, mask):
        print('CalculateRadiomicsFeatures._extract_features()')
        extractor = featureextractor.RadiomicsFeaturesExtractor(**self.get_param('settings'))
        extractor.enableAllFeatures()
        v = extractor.execute(image, mask)
        return v

    def _calculate_features(self, image, mask):
        print('CalculateRadiomicsFeatures._calculate_features()')
        i, m = self._load_image_and_mask(image, mask)
        v = self._extract_features(i, m)
        return v

    def _write_features(self, features, feature_file_path):
        with open(feature_file_path, 'w') as f:
            for k in features.keys():
                f.write(k + ' = ' + str(features[k]))
                f.write('\n')
        return feature_file_path

    def execute(self):
        print('CalculateRadiomicsFeatures.execute()')
        mask_file = self.get_input('mask_file')
        features = self._calculate_features(self.get_input('in_file'), mask_file)
        feature_file = os.path.split(mask_file)[1]
        feature_file = os.path.splitext(feature_file)[0] + '.txt'
        feature_file_path = os.path.join(self.get_param('out_dir'), 'PerPatient')
        os.makedirs(feature_file_path, exist_ok=True)
        feature_file_path = os.path.join(feature_file_path, feature_file)
        self._write_features(features, feature_file_path)
        self.set_output('out_file', feature_file_path)
