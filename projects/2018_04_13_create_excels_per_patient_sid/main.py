import os
import pandas as pd


if __name__ == '__main__':

    columns = [
        'display_text_NL',
        'display_text_DE',
        'rwth',
        'mumc',
        'value_type',
        'options',
        'default_option',
        'category_def',
    ]

    dd_file = '/Volumes/USB_SECURE1/Data/ESPRESSO/DataDict_LapLiver_v1.1.xlsx'
    dd_df = dfs = pd.read_excel(dd_file, 'Attributes', comment='#')
    dd_df.drop(columns, axis=1, inplace=True)
    print(dd_df.columns)

    out_dir = '/Volumes/USB_SECURE1/Data/ESPRESSO/Patients_LapLiver'

    id_file = '/Volumes/USB_SECURE1/Data/ESPRESSO/Biobank_Patiëntennummers_en_SIDs.xlsx'
    id_df = pd.read_excel(id_file, 'IDs', comment='#', index_col='SID')
    for idx, row in id_df.iterrows():
        if row['lap_liver'] == 1:
            f = '{}.xlsx'.format(idx)
            f = os.path.join(out_dir, f)
            dd_df.to_excel(f, index=False)
            print(f)
