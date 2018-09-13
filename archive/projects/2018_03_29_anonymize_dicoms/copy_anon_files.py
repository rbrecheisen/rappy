import os
import shutil
from rappy.utils import ArgParser


def get_file_path(src_dir):
    for root, dirs, files in os.walk(src_dir):
        for f in files:
            if f.endswith('.dcm'):
                return os.path.join(root, f)


def run(args):

    arg_parser = ArgParser()
    arg_parser.add_arg('ctp_dir')
    arg_parser.add_arg('tag_dir')
    arg_parser.add_arg('out_dir')
    arg_parser.add_arg('id_file')
    args = arg_parser.parse_args(args)

    random_ids = []
    with open(args['id_file'], 'r') as f:
        header = True
        for line in f.readlines():
            if header:
                header = False
                continue
            random_ids.append(line.strip())

    os.makedirs(args['out_dir'], exist_ok=True)

    for random_id in random_ids:
        file_path = get_file_path(os.path.join(args['ctp_dir'], random_id + '_dcm'))
        shutil.copyfile(
            file_path,
            os.path.join(args['out_dir'], random_id + '.dcm'))
        shutil.copyfile(
            os.path.join(args['tag_dir'], random_id + '.tag'),
            os.path.join(args['out_dir'], random_id + '.tag'))


if __name__ == '__main__':

    for name in ['David', 'Gregory']:
        run([
            '--ctp_dir=/Users/Ralph/Data/CTP/roots/FileStorageService',
            '--tag_dir=/Users/Ralph/Data/{}/Pancreas/Imaging/OriginalRenamed'.format(name),
            '--out_dir=/Users/Ralph/Data/{}/Pancreas/Imaging/OriginalRenamedAnonymized'.format(name),
            '--id_file=/Users/Ralph/Data/{}/Pancreas/Imaging/random_ids.csv'.format(name),
        ])
