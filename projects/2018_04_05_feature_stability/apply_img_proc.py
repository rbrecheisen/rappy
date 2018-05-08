import pydicom
from rappy.utils import ArgParser


def run(args):

    arg_parser = ArgParser()
    arg_parser.add_arg('in_file')
    args = arg_parser.parse_args(args)
    print(args)

    p = pydicom.read_file(args['in_file'])
    pixels = p.pixel_array
    # pixels_rescaled = rescale(pixels, 1.0/4.0)
    # print(pixels_rescaled.shape)


if __name__ == '__main__':
    run(['--in_file=/Users/Ralph/GoogleDrive/Dbx/FeatureStabilityAnalysis/David/S_0004473721.dcm'])
