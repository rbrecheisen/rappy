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


def print_types(df):
    tt = load_types()
    for c in df.columns:
        print('{}: {} ({})'.format(c, df[c].dtype, tt[c]))


def handle_Sex(df):
    df['Sex'] = df['Sex'].map({0: False, 1: True})
    return df


def handle_Death(df):
    df['Death'] = df['Death'].map({0: False, 1: True})
    return df


def handle_surgery(df):
    for i in range(5):
        df['surgery_{}'.format(i)] = (df['surgery'] == i)
    df = df.drop(['surgery'], axis=1)
    return df


def handle_Whipple_pppd(df):
    df['Whipple_pppd'] = df['Whipple_pppd'].map({0: False, 1: True})
    return df


def handle_DoubleBP(df):
    df['DoubleBP'] = df['DoubleBP'].map({0: False, 1: True})
    return df


def handle_Total_pancreatectomy(df):
    df['Total_pancreatectomy'] = df['Total_pancreatectomy'].map({0: False, 1: True})
    return df


def handle_Distal_pancreatectomy(df):
    df['Distal_pancreatectomy'] = df['Distal_pancreatectomy'].map({0: False, 1: True})
    return df


def handle_Open_close(df):
    df['Open_close'] = df['Open_close'].map({0: False, 1: True})
    return df


def handle_surgerycure(df):
    df['surgerycure'] = df['surgerycure'].map({0: False, 1: True})
    return df


def handle_Curatief_surg(df):
    df['Curatief_surg'] = df['Curatief_surg'].map({0: False, 1: True})
    return df


def handle_GPS(df):
    df['GPS_0'] = (df['GPS'] == 0)
    df['GPS_1'] = (df['GPS'] == 1)
    df['GPS_2'] = (df['GPS'] == 2)
    df['GPS_unknown'] = (df['GPS'] == 999)
    df = df.drop(['GPS'], axis=1)
    return df


def handle_PancFistula(df):
    df['PancFistula_0'] = (df['PancFistula'] == '0')
    df['PancFistula_1'] = (df['PancFistula'] == '1')
    df['PancFistula_2'] = (df['PancFistula'] == '2')
    df['PancFistula_3'] = (df['PancFistula'] == '3')
    df['PancFistula_unknown'] = (df['PancFistula'] == ' ')
    df = df.drop(['PancFistula'], axis=1)
    return df


def handle_PancFist_Y_N(df):
    df = df.drop(['PancFist_Y_N'], axis=1)
    return df


def handle_Infection_wound_total(df):
    df['Infection_wound_total'] = df['Infection_wound_total'].map({0: False, 1: True})
    return df


def handle_Infection_deep_POWI(df):
    df['Infection_deep_POWI'] = df['Infection_deep_POWI'].map({0: False, 1: True})
    return df


def handle_Infection_POWI(df):
    df['Infection_POWI'] = df['Infection_POWI'].map({0: False, 1: True})
    return df


def handle_Infection_deep_bile(df):
    df['Infection_deep_bile'] = df['Infection_deep_bile'].map({0: False, 1: True})
    return df


def handle_Infection_deep_fistula(df):
    df['Infection_deep_fistula'] = df['Infection_deep_fistula'].map({0: False, 1: True})
    return df


def handle_DGE(df):
    df['DGE_0'] = (df['DGE'] == 0)
    df['DGE_1'] = (df['DGE'] == 1)
    df['DGE_2'] = (df['DGE'] == 2)
    df['DGE_3'] = (df['DGE'] == 3)
    df['DGE_unknown'] = (df['DGE'] == 999)
    df = df.drop(['DGE'], axis=1)
    return df


def handle_DGE_y_n(df):
    df = df.drop(['DGE_y_n'], axis=1)
    return df


def handle_Pathology(df):
    df['Pathology_0'] = (df['Pathology'] == 0)
    df['Pathology_1'] = (df['Pathology'] == 1)
    df['Pathology_2'] = (df['Pathology'] == 2)
    df['Pathology_3'] = (df['Pathology'] == 3)
    df['Pathology_5'] = (df['Pathology'] == 5)
    df['Pathology_6'] = (df['Pathology'] == 6)
    df['Pathology_7'] = (df['Pathology'] == 7)
    df = df.drop(['Pathology'], axis=1)
    return df


def handle_PatPanc(df):
    df['PatPanc'] = df['PatPanc'].map({0: False, 1: True})
    return df


def handle_PatAmp(df):
    df['PatAmp'] = df['PatAmp'].map({0: False, 1: True})
    return df


def handle_PatChol(df):
    df['PatChol'] = df['PatChol'].map({0: False, 1: True})
    return df


def handle_PatDuo(df):
    df['PatDuo'] = df['PatDuo'].map({0: False, 1: True})
    return df


def handle_PatOth(df):
    df['PatOth'] = df['PatOth'].map({0: False, 1: True})
    return df


def handle_PatNone(df):
    df['PatNone'] = df['PatNone'].map({0: False, 1: True})
    return df


def handle_diabetes(df):
    df['diabetes_0'] = (df['diabetes'] == '0')
    df['diabetes_1'] = (df['diabetes'] == '0')
    df['diabetes_2'] = (df['diabetes'] == '0')
    df['diabetes_unknown'] = (df['diabetes'] == ' ')
    df = df.drop(['diabetes'], axis=1)
    return df


def handle_diabetes_yn(df):
    df = df.drop(['diabetes_yn'], axis=1)
    return df


def handle_comob_car(df):
    df['comob_car_0'] = (df['comob_car'] == '0')
    df['comob_car_1'] = (df['comob_car'] == '1')
    df['comob_car_unknown'] = (df['comob_car'] == ' ')
    df = df.drop(['comob_car'], axis=1)
    return df


def handle_comob_pul(df):
    df['comob_pul_0'] = (df['comob_pul'] == '0')
    df['comob_pul_1'] = (df['comob_pul'] == '1')
    df['comob_pul_unknown'] = (df['comob_pul'] == ' ')
    df = df.drop(['comob_pul'], axis=1)
    return df


def handle_comob_ren(df):
    df['comob_ren_0'] = (df['comob_ren'] == '0')
    df['comob_ren_1'] = (df['comob_ren'] == '1')
    df['comob_ren_unknown'] = (df['comob_ren'] == ' ')
    df = df.drop(['comob_ren'], axis=1)
    return df


def handle_CEP(df):
    df['CEP_0'] = (df['CEP'] == '0')
    df['CEP_1'] = (df['CEP'] == '1')
    df['CEP_unknown'] = (df['CEP'] == ' ')
    df = df.drop(['CEP'], axis=1)
    return df


def handle_Sepsis(df):
    df['Sepsis_0'] = (df['Sepsis'] == 0)
    df['Sepsis_1'] = (df['Sepsis'] == 1)
    df['Sepsis_unknown'] = (df['Sepsis'] == 999)
    df = df.drop(['Sepsis'], axis=1)
    return df


def handle_Gastrojejuno_leakage(df):
    df['Gastrojejuno_leakage'] = df['Gastrojejuno_leakage'].map({0: False, 1: True})
    return df


def handle_Hemorrhage(df):
    df['Hemorrhage'] = df['Hemorrhage'].map({0: False, 1: True})
    return df


def handle_Bile_leak(df):
    df['Bile_leak_0'] = (df['Bile_leak'] == 0)
    df['Bile_leak_1'] = (df['Bile_leak'] == 1)
    df['Bile_leak_unknown'] = (df['Bile_leak'] == 999)
    df = df.drop(['Bile_leak'], axis=1)
    return df


def handle_DelGasEmpt(df):
    df['DelGasEmpt_0'] = (df['DelGasEmpt'] == 0)
    df['DelGasEmpt_1'] = (df['DelGasEmpt'] == 1)
    df['DelGasEmpt_unknown'] = (df['DelGasEmpt'] == 999)
    df = df.drop(['DelGasEmpt'], axis=1)
    return df


def handle_Operative_mort(df):
    df['Operative_mort'] = df['Operative_mort'].map({0: False, 1: True})
    return df


def handle_Abscess(df):
    df['Abscess_0'] = (df['Abscess'] == 0)
    df['Abscess_1'] = (df['Abscess'] == 1)
    df['Abscess_unknown'] = (df['Abscess'] == 999)
    df = df.drop(['Abscess'], axis=1)
    return df


def handle_Fistula(df):
    df['Fistula'] = df['Fistula'].map({0: False, 1: True})
    return df


def handle_SSI_totalcat(df):
    df['SSI_totalcat_1'] = (df['SSI_totalcat'] == '1')
    df['SSI_totalcat_2'] = (df['SSI_totalcat'] == '2')
    df['SSI_totalcat_3'] = (df['SSI_totalcat'] == '3')
    df['SSI_totalcat_unknown'] = (df['SSI_totalcat'] == ' ')
    df = df.drop(['SSI_totalcat'], axis=1)
    return df


def handle_Age_surg(df):
    m = df['Age_surg'].median()
    df['Age_surg_L'] = (df['Age_surg'] < m)
    df['Age_surg_H'] = (df['Age_surg'] >= m)
    df = df.drop(['Age_surg'], axis=1)
    return df


def handle_Height(df):
    m = df['Height'].median()
    df['Height_L'] = (df['Height'] < m)
    df['Height_H'] = (df['Height'] >= m)
    df = df.drop(['Height'], axis=1)
    return df


def handle_BMI_pre(df):
    m = df['BMI_pre'].median()
    df['BMI_pre_L'] = (df['BMI_pre'] < m)
    df['BMI_pre_H'] = (df['BMI_pre'] >= m)
    df = df.drop(['BMI_pre'], axis=1)
    return df


def handle_Survival_month(df):
    m = df['Survival_month'].median()
    df['Survival_month_L'] = (df['Survival_month'] < m)
    df['Survival_month_H'] = (df['Survival_month'] >= m)
    df = df.drop(['Survival_month'], axis=1)
    return df


def handle_L3_muscleindex(df):
    m = df['L3_muscleindex'].median()
    df['L3_muscleindex_L'] = (df['L3_muscleindex'] < m)
    df['L3_muscleindex_H'] = (df['L3_muscleindex'] >= m)
    df = df.drop(['L3_muscleindex'], axis=1)
    return df


def handle_L3VAT_index(df):
    m = df['L3VAT_index'].median()
    df['L3VAT_index_L'] = (df['L3VAT_index'] < m)
    df['L3VAT_index_H'] = (df['L3VAT_index'] >= m)
    df = df.drop(['L3VAT_index'], axis=1)
    return df


def handle_L3SAT_index(df):
    m = df['L3SAT_index'].median()
    df['L3SAT_index_L'] = (df['L3SAT_index'] < m)
    df['L3SAT_index_H'] = (df['L3SAT_index'] >= m)
    df = df.drop(['L3SAT_index'], axis=1)
    return df


def handle_CT_Muscle(df):
    m = df['CT_Muscle'].median()
    df['CT_Muscle_L'] = (df['CT_Muscle'] < m)
    df['CT_Muscle_H'] = (df['CT_Muscle'] >= m)
    df = df.drop(['CT_Muscle'], axis=1)
    return df


def handle_CT_IMAT(df):
    # TODO: I was here!!!!!!
    return df


def handle_CT_VAT(df):
    return df


def handle_CT_SAT(df):
    return df


def handle_CT_MRA(df):
    return df


def handle_CRP(df):
    return df


def handle_Neutro(df):
    return df


def handle_Leuko(df):
    return df


def handle_Hb(df):
    return df


def handle_Bili(df):
    return df


def handle_ASAT(df):
    return df


def handle_ALAT(df):
    return df


def handle_LDH(df):
    return df


def handle_gGT(df):
    return df


def handle_AF(df):
    return df


def handle_Albumin(df):
    return df


def run():

    df = load_df()
    df = drop_columns(df)

    for c in df.columns:
        # Categorical features
        if c == 'Sex':
            df = handle_Sex(df)
        elif c == 'Death':
            df = handle_Death(df)
        elif c == 'surgery':
            df = handle_surgery(df)
        elif c == 'Whipple_pppd':
            df = handle_Whipple_pppd(df)
        elif c == 'DoubleBP':
            df = handle_DoubleBP(df)
        elif c == 'Total_pancreatectomy':
            df = handle_Total_pancreatectomy(df)
        elif c == 'Distal_pancreatectomy':
            df = handle_Distal_pancreatectomy(df)
        elif c == 'Open_close':
            df = handle_Open_close(df)
        elif c == 'surgerycure':
            df = handle_surgerycure(df)
        elif c == 'Curatief_surg':
            df = handle_Curatief_surg(df)
        elif c == 'GPS':
            df = handle_GPS(df)
        elif c == 'PancFistula':
            df = handle_PancFistula(df)
        elif c == 'PancFist_Y_N':
            df = handle_PancFist_Y_N(df)
        elif c == 'Infection_wound_total':
            df = handle_Infection_wound_total(df)
        elif c == 'Infection_deep_POWI':
            df = handle_Infection_deep_POWI(df)
        elif c == 'Infection_POWI':
            df = handle_Infection_POWI(df)
        elif c == 'Infection_deep_bile':
            df = handle_Infection_deep_bile(df)
        elif c == 'Infection_deep_fistula':
            df = handle_Infection_deep_fistula(df)
        elif c == 'DGE':
            df = handle_DGE(df)
        elif c == 'DGE_y_n':
            df = handle_DGE_y_n(df)
        elif c == 'Pathology':
            df = handle_Pathology(df)
        elif c == 'PatPanc':
            df = handle_PatPanc(df)
        elif c == 'PatAmp':
            df = handle_PatAmp(df)
        elif c == 'PatChol':
            df = handle_PatChol(df)
        elif c == 'PatDuo':
            df = handle_PatDuo(df)
        elif c == 'PatOth':
            df = handle_PatOth(df)
        elif c == 'PatNone':
            df = handle_PatNone(df)
        elif c == 'diabetes':
            df = handle_diabetes(df)
        elif c == 'diabetes_yn':
            df = handle_diabetes_yn(df)
        elif c == 'comob_car':
            df = handle_comob_car(df)
        elif c == 'comob_pul':
            df = handle_comob_pul(df)
        elif c == 'comob_ren':
            df = handle_comob_ren(df)
        elif c == 'CEP':
            df = handle_CEP(df)
        elif c == 'Sepsis':
            df = handle_Sepsis(df)
        elif c == 'Gastrojejuno_leakage':
            df = handle_Gastrojejuno_leakage(df)
        elif c == 'Hemorrhage':
            df = handle_Hemorrhage(df)
        elif c == 'Bile_leak':
            df = handle_Bile_leak(df)
        elif c == 'DelGasEmpt':
            df = handle_DelGasEmpt(df)
        elif c == 'Operative_mort':
            df = handle_Operative_mort(df)
        elif c == 'Abscess':
            df = handle_Abscess(df)
        elif c == 'Fistula':
            df = handle_Fistula(df)
        elif c == 'SSI_totalcat':
            df = handle_SSI_totalcat(df)
        # Numerical features
        elif c == 'Age_surg':
            df = handle_Age_surg(df)
        elif c == 'Height':
            df = handle_Height(df)
        elif c == 'BMI_pre':
            df = handle_BMI_pre(df)
        elif c == 'Survival_month':
            df = handle_Survival_month(df)
        elif c == 'L3_muscleindex':
            df = handle_L3_muscleindex(df)
        elif c == 'L3VAT_index':
            df = handle_L3VAT_index(df)
        elif c == 'L3SAT_index':
            df = handle_L3SAT_index(df)
        elif c == 'CT_Muscle':
            df = handle_CT_Muscle(df)
        elif c == 'CT_IMAT':
            df = handle_CT_IMAT(df)
        elif c == 'CT_VAT':
            df = handle_CT_VAT(df)
        elif c == 'CT_SAT':
            df = handle_CT_SAT(df)
        elif c == 'CT_MRA':
            df = handle_CT_MRA(df)
        elif c == 'CRP':
            df = handle_CRP(df)
        elif c == 'Neutro':
            df = handle_Neutro(df)
        elif c == 'Leuko':
            df = handle_Leuko(df)
        elif c == 'Hb':
            df = handle_Hb(df)
        elif c == 'Bili':
            df = handle_Bili(df)
        elif c == 'ASAT':
            df = handle_ASAT(df)
        elif c == 'ALAT':
            df = handle_ALAT(df)
        elif c == 'LDH':
            df = handle_LDH(df)
        elif c == 'gGT':
            df = handle_gGT(df)
        elif c == 'AF':
            df = handle_AF(df)
        elif c == 'Albumin':
            df = handle_Albumin(df)
        else:
            print('Skipping column {} (dtype: {})'.format(c, df[c].dtype))


if __name__ == '__main__':
    run()
