import os
import shutil


def run2():
    src_dir = '/Users/Ralph/Data/Gregory/Pancreas/Imaging/OriginalNewFormat'
    tar_dir = '/Users/Ralph/Data/Gregory/Pancreas/Imaging/OriginalRenamed'
    file_paths = []
    file_paths_new = []
    for root, dirs, files in os.walk(src_dir):
        for f in files:
            file_path = os.path.join(root, f)
            if '/L3/' in file_path:
                file_paths.append(file_path)
                file_path = file_path.replace(src_dir, '')
                file_path = file_path[1:]
                file_path = file_path.replace(' (L3)', '')
                file_path = file_path.replace('/L3/', '_')
                file_path = os.path.join(tar_dir, file_path)
                file_paths_new.append(os.path.join(tar_dir, file_path))
    os.makedirs(tar_dir, exist_ok=True)
    for i in range(len(file_paths)):
        shutil.copyfile(file_paths[i], file_paths_new[i])
        print('{} -> {}'.format(file_paths[i], file_paths_new[i]))


def run():
    src_dir = '/Users/Ralph/Data/Gregory/Pancreas/Imaging/Original'
    tar_dir = '/Users/Ralph/Data/Gregory/Pancreas/Imaging/OriginalRenamed'
    file_paths = []
    file_paths_new = []
    for root, dirs, files in os.walk(src_dir):
        for f in files:
            if 'IM_' not in f:
                continue
            file_path = os.path.join(root, f)
            if 'old' in file_path:
                continue
            file_paths.append(file_path)
            file_path = file_path.replace(src_dir, '')
            file_path = file_path[1:]
            file_path = file_path.replace(' case ', '')
            file_path = file_path.replace(os.sep, '_')
            file_path = os.path.join(tar_dir, file_path)
            file_paths_new.append(file_path)
    os.makedirs(tar_dir, exist_ok=True)
    for i in range(len(file_paths)):
        shutil.copyfile(file_paths[i], file_paths_new[i])
        print('{} -> {}'.format(file_paths[i], file_paths_new[i]))


if __name__ == '__main__':
    run()
    run2()
