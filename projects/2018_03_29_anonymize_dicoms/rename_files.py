import os
import shutil
from rappy.utils import ArgParser


def get_tag_file_path(dcm_file_path):
    base = os.path.splitext(dcm_file_path)
    return base[0] + '.tag'


def replace_with_random_id(file_path, random_id):
    path_items = os.path.split(file_path)
    file_name = path_items[-1]
    file_extension = os.path.splitext(file_name)[1]
    if file_extension == '':
        file_extension = '.dcm'
    return random_id + file_extension


def run(args):

    arg_parser = ArgParser()
    arg_parser.add_arg('src_dir')
    arg_parser.add_arg('out_dir')
    args = arg_parser.parse_args(args)

    data = {}

    # For each patient ID, load file path
    with open('{}/pat_id_file.csv'.format(args['src_dir']), 'r') as f:
        header = True
        for line in f.readlines():
            if header:
                header = False
                continue
            if line.startswith('#'):
                continue
            items = line.strip().split(',')
            data[items[0]] = [items[1]]

    # For each patient ID, load random ID
    with open('{}/pat_id_random_id.csv'.format(args['src_dir']), 'r') as f:
        header = True
        for line in f.readlines():
            if header:
                header = False
                continue
            if line.startswith('#'):
                continue
            items = line.strip().split(',')
            data[items[0]].append(items[1])

    os.makedirs(args['out_dir'], exist_ok=True)

    # Copy files to randomized new name
    for pat_id in data.keys():
        dcm_file_path = data[pat_id][0]
        tag_file_path = get_tag_file_path(dcm_file_path)
        random_id = data[pat_id][1]
        dcm_file_name = replace_with_random_id(dcm_file_path, random_id)
        tag_file_name = replace_with_random_id(tag_file_path, random_id)
        shutil.copyfile(dcm_file_path, os.path.join(args['out_dir'], dcm_file_name))
        shutil.copyfile(tag_file_path, os.path.join(args['out_dir'], tag_file_name))
        print('Renamed {}'.format(dcm_file_path))


if __name__ == '__main__':
    for name in ['David', 'Gregory']:
        run([
            '--src_dir=/Users/Ralph/Data/{}/Pancreas/Imaging'.format(name),
            '--out_dir=/Users/Ralph/Data/{}/Pancreas/Imaging/OriginalRenamed'.format(name),
        ])
