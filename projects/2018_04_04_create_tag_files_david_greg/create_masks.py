import os
import shutil
from rappy.radiomics import Dcm2Masks
from rappy.utils import ArgParser


def run(args):

    arg_parser = ArgParser()
    arg_parser.add_arg('src_dir')
    arg_parser.add_arg('out_dir')
    arg_parser.add_arg('label_map')
    args = arg_parser.parse_args(args)
    print(args)

    for f in os.listdir(args['src_dir']):
        if f.endswith('_tag.dcm'):
            sid = os.path.splitext(f)[0][:-4]
            tag_file = os.path.join(args['src_dir'], f)
            dcm_file = os.path.join(args['src_dir'], sid + '.dcm')
            dcm2masks = Dcm2Masks()
            dcm2masks.set_input('dcm_file', tag_file)
            dcm2masks.set_param('label_map', args['label_map'])
            dcm2masks.set_param('out_dir', args['out_dir'])
            out_files = dcm2masks.get_output('out_files')
            # Copy DICOM to output directory as well
            shutil.copyfile(dcm_file, os.path.join(args['out_dir'], sid + '.dcm'))
            print(out_files)


if __name__ == '__main__':

    for name in ['David', 'Gregory']:
        run([
            '--src_dir=/Users/Ralph/Data/{}/Pancreas/Imaging/OriginalRenamedAnonymizedTagConverted'.format(name),
            '--out_dir=/Users/Ralph/Data/{}/Pancreas/Imaging/OriginalRenamedAnonymizedTagConvertedMasks'.format(name),
            '--label_map={"1": "muscle", "5": "SAT", "7": "VAT"}'
        ])
