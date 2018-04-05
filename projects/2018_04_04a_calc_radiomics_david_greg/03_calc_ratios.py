import os
import pandas as pd
from rappy.utils import ArgParser


def run(args):

    arg_parser = ArgParser()
    arg_parser.add_arg('src_dir')
    arg_parser.add_arg('out_dir')
    args = arg_parser.parse_args(args)

    os.makedirs(args['out_dir'], exist_ok=True)

    print('Calculate ratios')
    fp = os.path.join(args['src_dir'], 'features_all.csv')
    df = pd.read_csv(fp, index_col='SID')

    tot_area = \
        df['muscle_original_shape_SurfaceArea'] + \
        df['SAT_original_shape_SurfaceArea'] + \
        df['VAT_original_shape_SurfaceArea']
    mus_area = df['muscle_original_shape_SurfaceArea']
    vat_area = df['VAT_original_shape_SurfaceArea']
    sat_area = df['SAT_original_shape_SurfaceArea']
    fat_area = \
        df['SAT_original_shape_SurfaceArea'] + \
        df['VAT_original_shape_SurfaceArea']

    columns = {
        'mus_tot': mus_area / tot_area,
        'vat_tot': vat_area / tot_area,
        'sat_tot': sat_area / tot_area,
        'fat_tot': fat_area / tot_area,
        'sat_vat': sat_area / vat_area,
        'mus_vat': mus_area / vat_area,
        'mus_sat': mus_area / sat_area,
        'mus_fat': mus_area / fat_area,
    }

    df = pd.DataFrame()
    df = df.from_dict({
        'mus_tot': columns['mus_tot'],
        'vat_tot': columns['vat_tot'],
        'sat_tot': columns['sat_tot'],
        'fat_tot': columns['fat_tot'],
        'sat_vat': columns['sat_vat'],
        'mus_vat': columns['mus_vat'],
        'mus_sat': columns['mus_sat'],
        'mus_fat': columns['mus_fat'],
    }, orient='columns')
    fp = os.path.join(args['src_dir'], 'features_area_ratios.csv')
    df.to_csv(fp, index=True)
    print(df.shape)


if __name__ == '__main__':

    for name in ['David', 'Gregory']:
        run([
            '--src_dir=/Users/Ralph/Data/{}/Pancreas/Imaging/RadiomicsFeatures'.format(name),
            '--out_dir=/Users/Ralph/Data/{}/Pancreas/Imaging/RadiomicsFeatures'.format(name),
        ])
