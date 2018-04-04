import os
from rappy.utils import ArgParser
from rappy.rad import CalculateRadiomicsFeatures


def run(args):

    arg_parser = ArgParser()
    arg_parser.add_arg('src_dir')
    arg_parser.add_arg('out_dir')
    args = arg_parser.parse_args(args)
    print(args)

    for tissue in ['muscle', 'SAT', 'VAT']:
        for f in os.listdir(args['src_dir']):
            expression = '_tag_{}.dcm'.format(tissue)
            if f.endswith(expression):
                sid = os.path.splitext(f)[0][:-(len(expression)-4)]
                in_file = os.path.join(args['src_dir'], sid + '.dcm')
                mask_file = os.path.join(args['src_dir'], sid + '_tag_{}.dcm'.format(tissue))
                crf = CalculateRadiomicsFeatures()
                crf.set_input('in_file', in_file)
                crf.set_input('mask_file', mask_file)
                crf.set_param('out_dir', args['out_dir'])
                out_file = crf.get_output('out_file')
                print(out_file)

    # Collect per-patient features in tissue-specific CSVs


if __name__ == '__main__':

    for name in ['David', 'Gregory']:
        run([
            '--src_dir=/Users/Ralph/Data/{}/Pancreas/Imaging/OriginalRenamedAnonymizedTagConvertedMasks'.format(name),
            '--out_dir=/Users/Ralph/Data/{}/Pancreas/Imaging/RadiomicsFeatures'.format(name),
        ])
