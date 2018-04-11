import os
from rappy.utils import ArgParser


def run(args):

    arg_parser = ArgParser()
    arg_parser.add_arg('src_file')
    arg_parser.add_arg('out_file')
    args = arg_parser.parse_args(args)
    print(args)

    lines = []
    with open(args['src_file'], 'r') as f:
        for line in f.readlines():
            line = line.strip()
            ix = line.split(',')[0]
            fp = line.split(',')[1]
            fn = os.path.split(fp)[1]
            lines.append([ix, fn])

    with open(args['out_file'], 'w') as f:
        for line in lines:
            f.write('{},{}\n'.format(line[0], line[1]))


if __name__ == '__main__':

    run([
        '--src_file=/Volumes/NO NAME/Data/Gregory/Pancreas/Imaging/pat_id_file.csv',
        '--out_file=/Volumes/NO NAME/Data/Gregory/Pancreas/Imaging/patid_filename.csv',
    ])
