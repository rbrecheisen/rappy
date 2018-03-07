import json
import pandas as pd
import numpy as np


def load_df():
    directory = ''
    directory += '/Users/Ralph/GoogleDrive/Documenten/Projecten/Chirurgie/Projecten'
    directory += '/ESPRESSO/DataDictionary/David'
    directory += '/151210 DVD Sarcopenia analysis_newcorrect.csv'
    df = pd.read_csv(directory, index_col=False)
    return df


def drop_columns(df):
    columns = [
        'ID', 'Weightloss_perc', 'Survival_dead', 'Survival_live', 'Survival_weeks', 'Survival', 'Follow_up', 'S90d_mort',
        'S1y_mort', 'L3index_control', 'L3IMAT_index', 'Sarcopenia_martin', 'LowRadAtt_martin', 'Sarcopenia_median',
        'Sarcopenia_low33', 'LowMAI_median', 'lowMAI_33', 'high_imat_median', 'high_imat_67', 'highSAT_median',
        'High_SAT_67', 'HighVAT_median', 'High67_VAT', 'HighVATindex', 'High67VATindex', 'Sarcopenic_overweight_median',
        'L3muscle_tertile', 'L3VAT_tertile', 'CTIMAT_tertile', 'CTSAT_tertile', 'CTMAI_tertile',
        'Infection_deep_abscess', 'filter_$', 'Selection_pancreas', 'BMI_cat', 'Weightloss_cat', 'Old_Pathology',
        'Path_SAT', 'CEP_noOpMort', 'overweight', 'obese', 'overweight_sarcopenia', 'obese_sarcopenia', 'Muscle_low33',
        'VAT_High33', 'SAT_High33', 'IMAT_High33', 'Muscle_L3_low33', 'VAT_L3_High33', 'SAT_L3_High33', 'MRA_low33',
        'VAT_L3_low33', 'SAT_L3_low33', 'CT_MAI_10', 'CT_MAI_20', 'CT_MAI_30', 'CT_MAI_40', 'CT_MAI_50', 'CT_MAI_60',
        'CT_MAI_70', 'CT_MAI_80', 'CT_MAI_90', 'Weightloss_025', 'L3_muscleindex_10', 'L3_muscleindex_20',
        'L3_muscleindex_30', 'L3_muscleindex_40', 'L3_muscleindex_50', 'L3_muscleindex_60', 'L3_muscleindex_70',
        'L3_muscleindex_80', 'L3_muscleindex_90', 'XBE_1_MULTCOXSURV', 'PRE_1_MULTLOGCEP', 'PRE_2_MULTLOGSSI',
        'Age_70', 'VATMRA', 'MuscleMRA', 'AGEMRA', 'Age_Cat', 'L3_muscle_Zscore', 'MRA_Zscore', 'L3_VAT_Zscore',
        'L3Zscore_cat', 'MRAZscore_cat', 'L3_VAT_Zscore_cat', 'MRA_Zscore_nosex', 'MRA_Zscore_nosex_Cat',
        'MRA_Ztertile', 'MRA_zscore_tertile_nosex', 'MRA_zscore2SDlow']
    return df.drop(columns, axis=1)


def load_types():
    return {
        'Sex': 'boolean', 'Age_surg': 'numeric', 'Height': 'numeric', 'BMI_pre': 'numeric', 'Death': 'boolean',
        'Survival_month': 'numeric', 'L3_muscleindex': 'numeric', 'L3VAT_index': 'numeric', 'L3SAT_index': 'numeric',
        'CT_Muscle': 'numeric', 'CT_IMAT': 'numeric', 'CT_VAT': 'numeric', 'CT_SAT': 'numeric', 'CT_MRA': 'numeric',
        'surgery': 'categorical', 'Whipple_pppd': 'boolean', 'DoubleBP': 'boolean', 'Total_pancreatectomy': 'boolean',
        'Distal_pancreatectomy': 'boolean', 'Open_close': 'boolean', 'surgerycure': 'boolean',
        'Curatief_surg': 'boolean', 'GPS': 'categorical', 'CRP': 'numeric', 'Neutro': 'numeric', 'Leuko': 'numeric',
        'Hb': 'numeric', 'Bili': 'numeric', 'ASAT': 'numeric', 'ALAT': 'numeric', 'LDH': 'numeric', 'gGT': 'numeric',
        'AF': 'numeric', 'Albumin': 'numeric', 'PancFistula': 'categorical', 'PancFist_Y_N': 'boolean',
        'Infection_wound_total': 'boolean', 'Infection_deep_POWI': 'boolean', 'Infection_POWI': 'boolean',
        'Infection_deep_bile': 'boolean', 'Infection_deep_fistula': 'boolean', 'DGE': 'categorical',
        'DGE_y_n': 'boolean', 'Pathology': 'categorical', 'PatPanc': 'boolean', 'PatAmp': 'boolean',
        'PatChol': 'boolean', 'PatDuo': 'boolean', 'PatOth': 'boolean', 'PatNone': 'boolean', 'diabetes': 'categorical',
        'diabetes_yn': 'categorical', 'comob_car': 'categorical', 'comob_pul': 'categorical',
        'comob_ren': 'categorical', 'CEP': 'categorical', 'Sepsis': 'categorical', 'Gastrojejuno_leakage': 'boolean',
        'Hemorrhage': 'boolean', 'Bile_leak': 'categorical', 'DelGasEmpt': 'categorical', 'Operative_mort': 'boolean',
        'Abscess': 'categorical', 'Fistula': 'boolean', 'SSI_totalcat': 'categorical'}


def run():
    df = load_df()
    df = drop_columns(df)
    print(df)


if __name__ == '__main__':
    run()
