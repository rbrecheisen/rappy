import sys
import os
import shutil


def get_file_path(src_dir):
    for root, dirs, files in os.walk(src_dir):
        for f in files:
            if f.endswith('.dcm'):
                return os.path.join(root, f)


def get_arg_map(args):
    if len(args) != 4:
        return None
    names = ['--ctp_dir', '--tag_dir', '--target_dir', '--random_id_file']
    arg_map = {}
    for a in args:
        k, v = a.split('=')[0], a.split('=')[1]
        if k not in names:
            return None
        arg_map[k[2:]] = v
    return arg_map


def get_help():
    text = ''
    text += '\n\nUsage:\n'
    text += 'copy_anon_files.py\n'
    text += '  --ctp_dir=<dir path>\n'
    text += '  --tag_dir=<dir path>\n'
    text += '  --target_dir=<dir path>\n'
    text += '  --random_id_file=<file path>\n'
    text += '\n'
    return text


def run(args):

    arg_map = get_arg_map(args)
    if not arg_map:
        raise RuntimeError(get_help())

    random_ids = []
    with open(arg_map['random_id_file'], 'r') as f:
        header = True
        for line in f.readlines():
            if header:
                header = False
                continue
            random_ids.append(line.strip().split(',')[1])

    os.makedirs(arg_map['target_dir'], exist_ok=True)

    for random_id in random_ids:
        file_path = get_file_path(os.path.join(arg_map['ctp_dir'], random_id + '_dcm'))
        shutil.copyfile(
            file_path,
            os.path.join(arg_map['target_dir'], random_id + '.dcm'))
        shutil.copyfile(
            os.path.join(arg_map['tag_dir'], random_id + '.tag'),
            os.path.join(arg_map['target_dir'], random_id + '.tag'))


if __name__ == '__main__':

    arg1 = '--ctp_dir=/Users/Ralph/Data/CTP/roots/FileStorageService'
    arg2 = '--tag_dir=/Users/Ralph/Data/Gregory/Pancreas/Imaging/OriginalRenamed'
    arg3 = '--target_dir=/Users/Ralph/Data/Gregory/Pancreas/Imaging/OriginalRenamedAnonymized'
    arg4 = '--random_id_file=/Users/Ralph/Data/{}/Pancreas/Imaging/random_ids.csv'

    run([arg1, arg2, arg3, arg4])
    # run(sys.argv)
