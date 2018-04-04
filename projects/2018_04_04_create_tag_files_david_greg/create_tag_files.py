import shutil
import os
from rappy.radiomics import Tag2Dcm
from rappy.utils import ArgParser


def run(args):

    arg_parser = ArgParser()
    arg_parser.add_arg('src_dir')
    arg_parser.add_arg('out_dir')
    args = arg_parser.parse_args(args)

    for f in os.listdir(args['src_dir']):
        if f.endswith('.dcm'):
            sid = os.path.splitext(f)[0]
            tag_file = os.path.join(args['src_dir'], sid + '.tag')
            dcm_file = os.path.join(args['src_dir'], sid + '.dcm')
            # Convert TAG file to DICOM
            tag2dcm = Tag2Dcm()
            tag2dcm.set_input('tag_file', tag_file)
            tag2dcm.set_input('dcm_file', dcm_file)
            tag2dcm.set_param('out_dir', args['out_dir'])
            out_file = tag2dcm.get_output('out_file')
            # Copy DICOM to output directory as well
            shutil.copyfile(dcm_file, os.path.join(args['out_dir'], sid + '.dcm'))
            print(out_file)


if __name__ == '__main__':

    for name in ['David', 'Gregory']:
        run([
            '--src_dir=/Users/Ralph/Data/{}/Pancreas/Imaging/OriginalRenamedAnonymized'.format(name),
            '--out_dir=/Users/Ralph/Data/{}/Pancreas/Imaging/OriginalRenamedAnonymizedTagConverted'.format(name),
        ])
