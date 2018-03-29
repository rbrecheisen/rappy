import os
import shutil


def get_file_path(src_dir):
    for root, dirs, files in os.walk(src_dir):
        for f in files:
            if f.endswith('.dcm'):
                return os.path.join(root, f)


def run():

    name = 'David'
    src_dir = '/Users/Ralph/Data/CTP/roots/FileStorageService'
    dst_dir = '/Users/Ralph/Data/{}/Pancreas/Imaging/OriginalRenamedAnonymized'.format(name)
    random_ids = []

    with open('/Users/Ralph/Data/{}/Pancreas/Imaging/pat_id_random_id.csv'.format(name), 'r') as f:
        header = True
        for line in f.readlines():
            if header:
                header = False
                continue
            random_ids.append(line.strip().split(',')[1])
    os.makedirs(dst_dir, exist_ok=True)
    for random_id in random_ids:
        file_path = get_file_path(os.path.join(src_dir, random_id + '_dcm'))
        shutil.copyfile(file_path, os.path.join(dst_dir, random_id + '.dcm'))


if __name__ == '__main__':
    run()
