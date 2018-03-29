import os


def run():

    dir_davi = '/Users/Ralph/Data/David/Pancreas/Imaging/Original'
    dir_greg = '/Users/Ralph/Data/Gregory/Pancreas/Imaging/OriginalFlattened'

    # file_paths = []
    # for f in os.listdir(dir_davi):
    #     if '.dcm' in f:
    #         file_paths.append(os.path.join(dir_davi, f))
    #
    # pat_ids = []
    # with open('{}/../pat_id_file.csv'.format(dir_davi), 'w') as f:
    #     f.write('pat_id,file_path\n')
    #     for file_path in file_paths:
    #         items = os.path.split(file_path)
    #         file_name = items[-1]
    #         idx = file_name.split('-')[0]
    #         if idx in pat_ids:
    #             raise RuntimeError('ID already in list')
    #         pat_ids.append(idx)
    #         f.write('{},{}\n'.format(idx, file_path))
    #
    # random_ids = []
    # with open('{}/../random_ids.csv'.format(dir_davi), 'r') as f:
    #     for line in f.readlines():
    #         random_ids.append(line.strip())
    # if len(pat_ids) != len(random_ids):
    #     raise RuntimeError('Wrong number of IDs ({}, {})'.format(len(pat_ids), len(random_ids)))
    # with open('{}/../pat_id_random_id.csv'.format(dir_davi), 'w') as f:
    #     f.write('pat_id,random_id\n')
    #     for i in range(len(pat_ids)):
    #         f.write('{},{}\n'.format(pat_ids[i], random_ids[i]))

    file_paths = []
    pat_ids = []
    for f in os.listdir(dir_greg):
        if '.tag' not in f:
            file_paths.append(os.path.join(dir_greg, f))
    with open('{}/../pat_id_file.csv'.format(dir_greg), 'w') as f:
        f.write('pat_id,file_path\n')
        for file_path in file_paths:
            pat_id = os.path.split(file_path)[-1]
            pat_ids.append(pat_id)
            f.write('{},{}\n'.format(pat_id, file_path))
    random_ids = []
    with open('{}/../random_ids.csv'.format(dir_greg), 'r') as f:
        for line in f.readlines():
            random_ids.append(line.strip())
    if len(pat_ids) != len(random_ids):
        raise RuntimeError('Wrong number of IDs ({}, {})'.format(len(pat_ids), len(random_ids)))
    with open('{}/../pat_id_random_id.csv'.format(dir_greg), 'w') as f:
        f.write('pat_id,random_id\n')
        for i in range(len(pat_ids)):
            f.write('{},{}\n'.format(pat_ids[i], random_ids[i]))


if __name__ == '__main__':
    run()
