import os
import shutil
import pydicom
import numpy as np


def get_coordinates(file_path, label):
    p = pydicom.read_file(open(file_path, 'rb'))
    pixels = p.pixel_array
    coordinates = []
    for i in range(pixels.shape[0]):
        for j in range(pixels.shape[1]):
            if pixels[i, j] == label:
                coordinates.append((i, j))
    return coordinates


def get_key(f):
    elements = f.split('_')
    return elements[0]


def check_uniqueness_coordinates(coordinates):
    nrs = []
    for coordinate in coordinates:
        nrs.append(str(coordinate[0]) + str(coordinate[1]))
    arr = np.array(nrs)
    print('{} == {}'.format(len(arr), len(np.unique(arr))))
    return len(arr) == len(np.unique(arr))


def calculate_coordinates(src_dir, target_dir, overwrite=True):
    if overwrite:
        shutil.rmtree(target_dir, ignore_errors=True)
        os.makedirs(target_dir)
    d = dict()
    for root, dirs, files in os.walk(src_dir):
        for f in files:
            if f.endswith('_tag_rest.dcm') or f.endswith('_tag_minor.dcm') or f.endswith('_tag_major.dcm'):
                key = get_key(f)
                if key not in d.keys():
                    d[key] = []
                d[key].append(os.path.join(root, f))
    for key in d.keys():
        coordinates = []
        for f in d[key]:
            # Each mask file has only 0's and 1's so we look for 1's...
            coordinates.extend(get_coordinates(f, 1))
        print('Found {} coordinates for {}'.format(len(coordinates), key))
        if check_uniqueness_coordinates(coordinates):
            print('Writing to file...')
            with open(os.path.join(target_dir, 'coordinates_{}.txt'.format(key)), 'w') as f:
                for coordinate in coordinates:
                    f.write('{}, {}\n'.format(coordinate[0], coordinate[1]))
        else:
            raise RuntimeError('Coordinates not unique!')


def get_dcm_file_path(dcm_dir, f):
    base = os.path.splitext(f.split('_')[1])[0]
    dcm_file = os.path.join(dcm_dir, base + '.dcm')
    return dcm_file


def get_pixel_values(coordinate_file_path, dcm_file_path):
    p = dicom.read_file(open(dcm_file_path, 'rb'))
    # Some files have intercept != 0 or slope != 1
    intercept = p[0x0028, 0x1052].value
    slope = p[0x0028, 0x1053].value
    pixels = p.pixel_array
    pixel_values = []
    with open(coordinate_file_path, 'r') as f:
        for line in f.readlines():
            elements = [x.strip() for x in line.split(',')]
            i = int(elements[0])
            j = int(elements[1])
            pixel_values.append(intercept + slope * pixels[i, j])
    return pixel_values


def calculate_mean_hounds_field_units(dcm_dir, coordinates_dir, target_dir):
    means = {}
    for root, dirs, files in os.walk(coordinates_dir):
        for f in files:
            if f.startswith('coordinates'):
                key = f.split('_')[1].split('.')[0]
                if key not in means.keys():
                    means[key] = 0.0
                dcm_file_path = get_dcm_file_path(dcm_dir, f)
                print('Processing {}...'.format(dcm_file_path))
                pixel_values = get_pixel_values(os.path.join(root, f), dcm_file_path)
                arr = np.array(pixel_values)
                means[key] = arr.mean()
    with open(os.path.join(target_dir, 'MeanHUs.csv'), 'w') as f:
        f.write('File, MeanHU\n')
        for key in means.keys():
            f.write('{}, {}\n'.format(key, means[key]))


if __name__ == '__main__':

    # calculate_coordinates(
    #     src_dir='/Users/Ralph/Data/Gregory/ColorectalMets/Imaging/OriginalFixedTagConvertedMasks',
    #     target_dir='/Users/Ralph/Data/Gregory/ColorectalMets/Imaging/HU',
    #     overwrite=True)

    calculate_mean_hounds_field_units(
        dcm_dir='/Users/Ralph/Data/Gregory/ColorectalMets/Imaging/OriginalFixedTagConverted',
        coordinates_dir='/Users/Ralph/Data/Gregory/ColorectalMets/Imaging/HU',
        target_dir='/Users/Ralph/Data/Gregory/ColorectalMets/Imaging')
