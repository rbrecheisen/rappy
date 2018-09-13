import os
import sys
# from rappy.utils import ArgParser


def run(args):

    # arg_parser = ArgParser()
    # arg_parser.add_arg('dir')
    # args = arg_parser.parse_args(args)
    if len(args) != 2:
        print('add_dcm_ext_to_dicoms_greg.py --dir=<root directory to dicoms>')
        return

    d = args[1]

    for root, dirs, files in os.walk(d):
        for f in files:
            if f.startswith('IM_'):
                f = os.path.join(root, f)
                f_new = f + '.dcm'
                os.rename(f, f_new)
                print('Renamed {} -> {}'.format(f, f_new))


if __name__ == '__main__':
    # run(['--dir=/Volumes/USB_SECURE1/Data/Gregory/Pancreas/Imaging/OriginalOther/Test'])
    run(sys.argv)
