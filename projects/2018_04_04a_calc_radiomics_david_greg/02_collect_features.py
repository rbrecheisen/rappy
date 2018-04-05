import os
import pandas as pd
from rappy.utils import ArgParser


def get_row(file_path):
    row = []
    columns = []
    with open(file_path, 'r') as f:
        for line in [x.strip() for x in f.readlines()]:
            if line.startswith('original'):
                items = line.split(' = ')
                row.append(items[1])
                columns.append(items[0])
    return row, columns


def run(args):

    arg_parser = ArgParser()
    arg_parser.add_arg('src_dir')
    arg_parser.add_arg('out_dir')
    args = arg_parser.parse_args(args)

    os.makedirs(args['out_dir'], exist_ok=True)

    print('Create feature file per tissue')
    for tissue in ['muscle', 'SAT', 'VAT']:
        body = []
        index = []
        header = None
        for f in os.listdir(args['src_dir']):
            expression = '_tag_{}.txt'.format(tissue)
            if f.endswith(expression):
                sid = os.path.splitext(f)[0][:-(len(expression)-4)]
                index.append(sid)
                feature_file = os.path.join(args['src_dir'], f)
                row, cols = get_row(feature_file)
                if not header:
                    header = cols
                body.append(row)
        fp = os.path.join(args['out_dir'], 'features_{}.csv'.format(tissue))
        df = pd.DataFrame(data=body, columns=header, index=index)
        df.index.name = 'SID'
        df.to_csv(fp, index=True)
        # print(fp)

    print('Creating feature file for ALL tissues')
    dfs = []
    for tissue in ['muscle', 'SAT', 'VAT']:
        fp = os.path.join(args['out_dir'], 'features_{}.csv'.format(tissue))
        df = pd.read_csv(fp, index_col='SID')
        df.columns = ['{}_'.format(tissue) + c for c in df.columns]
        dfs.append(df)
    fp = os.path.join(args['out_dir'], 'features_all.csv')
    df = pd.concat(dfs, axis=1)
    df.index.name = 'SID'
    df.to_csv(fp, index=True)


if __name__ == '__main__':

    for name in ['David', 'Gregory']:
        run([
            '--src_dir=/Users/Ralph/Data/{}/Pancreas/Imaging/RadiomicsFeatures/PerPatient'.format(name),
            '--out_dir=/Users/Ralph/Data/{}/Pancreas/Imaging/RadiomicsFeatures'.format(name),
        ])
