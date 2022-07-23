import pandas as pd
import numpy as np


class JusticeNumbers:
    def __init__(self, year=2020, branch='electoral'):
        self.year = year
        self.branch = branch

    def loadNewCases(self):
        """Class method to load indicator data related to new cases (lawsuits) from CSV files.

        Returns:
            pandas.DataFrame: data from indicators related to new cases (lawsuits) of all instances of jurisdiction of
                              the Brazilian electoral justice.
        """


        # New Cases (lawsuits)
        df_cn_3g = pd.read_excel("painelcnj/indicadores/Cn-3g.xlsx", usecols = ['JN - Ano', 'Total'],
                    thousands = '.', converters = {'JN - Ano': np.int32, 'Total': np.int32})
        df_cn_3g.insert(0, 'instance', '3')
        df_cn_2g = pd.read_excel("painelcnj/indicadores/Cn-2g.xlsx", usecols = ['JN - Ano', 'Total'],
                    thousands = '.', converters = {'JN - Ano': np.int32, 'Total': np.int32})
        df_cn_2g.insert(0, 'instance', '2')
        df_cn_1g = pd.read_excel("painelcnj/indicadores/Cn-1g.xlsx", usecols = ['JN - Ano', 'Total'],
                    thousands = '.', converters = {'JN - Ano': np.int32, 'Total': np.int32})
        df_cn_1g.insert(0, 'instance', '1')
        df_cn = pd.concat([df_cn_3g, df_cn_2g, df_cn_1g])
        df_cn = df_cn.rename(
            columns={"Total": "new_cases", "JN - Ano": "year"})
        df_cn['instance'] = df_cn['instance'].replace(
            ['Tribunal superior', '2º grau', '1º grau'],
            ['3', '2', '1'])
        df_cn.set_index(['instance', 'year'], inplace=True)


        # original competence - new original cases
        df_cno_3g = pd.read_excel("painelcnj/indicadores/Cno-3g.xlsx", usecols = ['JN - Ano', 'Total'],
                    thousands = '.', converters = {'JN - Ano': np.int32, 'Total': np.int32})
        df_cno_3g.insert(0, 'instance', '3')
        df_cno_2g = pd.read_excel("painelcnj/indicadores/Cno-2g.xlsx", usecols = ['JN - Ano', 'Total'],
                    thousands = '.', converters = {'JN - Ano': np.int32, 'Total': np.int32})
        df_cno_2g.insert(0, 'instance', '2')
        df_cno_1g = pd.read_excel("painelcnj/indicadores/Cno-1g.xlsx", usecols = ['JN - Ano', 'Total'],
                    thousands = '.', converters = {'JN - Ano': np.int32, 'Total': np.int32})
        df_cno_1g.insert(0, 'instance', '1')

        df_cno = pd.concat([df_cno_3g, df_cno_2g, df_cno_1g])
        df_cno.rename(columns={"Total": "original_cases", "JN - Ano": "year"}, inplace=True)
        df_cno.set_index(['instance', 'year'], inplace=True)

        # appeal competence - new appeal cases
        df_cnr_3g = pd.read_excel("painelcnj/indicadores/Cnr-3g.xlsx", usecols = ['JN - Ano', 'Total'],
                    thousands = '.', converters = {'JN - Ano': np.int32, 'Total': np.int32})
        df_cnr_3g.insert(0, 'instance', '3')
        df_cnr_2g = pd.read_excel("painelcnj/indicadores/Cnr-2g.xlsx", usecols = ['JN - Ano', 'Total'],
                    thousands = '.', converters = {'JN - Ano': np.int32, 'Total': np.int32})
        df_cnr_2g.insert(0, 'instance', '2')

        df_cnr = pd.concat([df_cnr_3g, df_cnr_2g])
        df_cnr.rename(columns={"Total": "appeal_cases", "JN - Ano": "year"}, inplace=True)
        df_cnr.set_index(['instance', 'year'], inplace=True)

        # original competence - new original cases
        df_cnelet_3g = pd.read_excel("painelcnj/indicadores/CnElet-3g.xlsx", usecols = ['JN - Ano', 'Total'],
                    thousands = '.', converters = {'JN - Ano': np.int32, 'Total': np.int32})
        df_cnelet_3g.insert(0, 'instance', '3')
        df_cnelet_2g = pd.read_excel("painelcnj/indicadores/CnElet-2g.xlsx", usecols = ['JN - Ano', 'Total'],
                    thousands = '.', converters = {'JN - Ano': np.int32, 'Total': np.int32})
        df_cnelet_2g.insert(0, 'instance', '2')
        df_cnelet_1g = pd.read_excel("painelcnj/indicadores/CnElet-1g.xlsx", usecols = ['JN - Ano', 'Total'],
                    thousands = '.', converters = {'JN - Ano': np.int32, 'Total': np.int32})
        df_cnelet_1g.insert(0, 'instance', '1')

        df_cnelet = pd.concat([df_cnelet_3g, df_cnelet_2g, df_cnelet_1g])
        df_cnelet.rename(columns={"Total": "eletronic_cases", "JN - Ano": "year"}, inplace=True)
        df_cnelet.set_index(['instance', 'year'], inplace=True)

        # finished cases
        df_tbaix_3g = pd.read_excel("painelcnj/indicadores/TBaix-3g.xlsx", usecols = ['JN - Ano', 'Total'],
                    thousands = '.', converters = {'JN - Ano': np.int32, 'Total': np.int32})
        df_tbaix_3g.insert(0, 'instance', '3')
        df_tbaix_2g = pd.read_excel("painelcnj/indicadores/TBaix-2g.xlsx", usecols = ['JN - Ano', 'Total'],
                    thousands = '.', converters = {'JN - Ano': np.int32, 'Total': np.int32})
        df_tbaix_2g.insert(0, 'instance', '2')
        df_tbaix_1g = pd.read_excel("painelcnj/indicadores/TBaix-1g.xlsx", usecols = ['JN - Ano', 'Total'],
                    thousands = '.', converters = {'JN - Ano': np.int32, 'Total': np.int32})
        df_tbaix_1g.insert(0, 'instance', '1')

        df_tbaix = pd.concat([df_tbaix_3g, df_tbaix_2g, df_tbaix_1g])
        df_tbaix.rename(columns={"Total": "finished_cases", "JN - Ano": "year"}, inplace=True)
        df_tbaix.set_index(['instance', 'year'], inplace=True)

        # pendent cases
        df_cp_3g = pd.read_excel("painelcnj/indicadores/Dec-3g.xlsx", usecols = ['JN - Ano', 'Total'],
                    thousands = '.', converters = {'JN - Ano': np.int32, 'Total': np.int32})
        df_cp_3g.insert(0, 'instance', '3')
        df_cp_2g = pd.read_excel("painelcnj/indicadores/Dec-2g.xlsx", usecols = ['JN - Ano', 'Total'],
                    thousands = '.', converters = {'JN - Ano': np.int32, 'Total': np.int32})
        df_cp_2g.insert(0, 'instance', '2')
        df_cp_1g = pd.read_excel("painelcnj/indicadores/Dec-1g.xlsx", usecols = ['JN - Ano', 'Total'],
                    thousands = '.', converters = {'JN - Ano': np.int32, 'Total': np.int32})
        df_cp_1g.insert(0, 'instance', '1')

        df_cp = pd.concat([df_cp_3g, df_cp_2g, df_cp_1g])
        df_cp.rename(columns={"Total": "pendent_cases", "JN - Ano": "year"}, inplace=True)
        df_cp.set_index(['instance', 'year'], inplace=True)

        # decision cases
        df_dec_3g = pd.read_excel("painelcnj/indicadores/Cp-3g.xlsx", usecols = ['JN - Ano', 'Total'],
                    thousands = '.', converters = {'JN - Ano': np.int32, 'Total': np.int32})
        df_dec_3g.insert(0, 'instance', '3')
        df_dec_2g = pd.read_excel("painelcnj/indicadores/Cp-2g.xlsx", usecols = ['JN - Ano', 'Total'],
                    thousands = '.', converters = {'JN - Ano': np.int32, 'Total': np.int32})
        df_dec_2g.insert(0, 'instance', '2')
        df_dec_1g = pd.read_excel("painelcnj/indicadores/Cp-1g.xlsx", usecols = ['JN - Ano', 'Total'],
                    thousands = '.', converters = {'JN - Ano': np.int32, 'Total': np.int32})
        df_dec_1g.insert(0, 'instance', '1')

        df_dec = pd.concat([df_dec_3g, df_dec_2g, df_dec_1g])
        df_dec.rename(columns={"Total": "decisions_cases", "JN - Ano": "year"}, inplace=True)
        df_dec.set_index(['instance', 'year'], inplace=True)

        # suspend cases
        df_sus_3g = pd.read_excel("painelcnj/indicadores/Sus-3g.xlsx", usecols = ['JN - Ano', 'Total'],
                    thousands = '.', converters = {'JN - Ano': np.int32, 'Total': np.int32})
        df_sus_3g.insert(0, 'instance', '3')
        df_sus_2g = pd.read_excel("painelcnj/indicadores/Sus-2g.xlsx", usecols = ['JN - Ano', 'Total'],
                    thousands = '.', converters = {'JN - Ano': np.int32, 'Total': np.int32})
        df_sus_2g.insert(0, 'instance', '2')
        df_sus_1g = pd.read_excel("painelcnj/indicadores/Sus-1g.xlsx", usecols = ['JN - Ano', 'Total'],
                    thousands = '.', converters = {'JN - Ano': np.int32, 'Total': np.int32})
        df_sus_1g.insert(0, 'instance', '1')

        df_sus = pd.concat([df_sus_3g, df_sus_2g, df_sus_1g])
        df_sus.rename(columns={"Total": "suspended_cases", "JN - Ano": "year"}, inplace=True)
        df_sus.set_index(['instance', 'year'], inplace=True)

        # Merge Datasets
        df_result = pd.merge(df_cn, df_cno,  how="outer", on=["instance", "year"])
        df_result = df_result.merge(df_cnr,  how="outer", on=["instance", "year"])
        df_result = df_result.merge(df_cnelet, how="outer", on=["instance", "year"])
        df_result = df_result.merge(df_tbaix, how="outer", on=["instance", "year"])
        df_result = df_result.merge(df_cp, how="outer", on=["instance", "year"])
        df_result = df_result.merge(df_dec, how="outer", on=["instance", "year"])
        df_result = df_result.merge(df_sus, how="outer", on=["instance", "year"])
        # df_result = df_result.fillna(-1)

        return df_result

    def loadInternalAppeals(self):
        """Class method to load indicator data related to internal appeals from CSV files.

        Returns:
            pandas.DataFrame: data from indicators related to internal appeals of all instances of jurisdiction of
                              the Brazilian electoral justice.
        """

        # new internal appeals
        df_rint_1g = pd.read_excel("painelcnj/indicadores/Rint-1g.xlsx", usecols=['JN - Ano', 'Total'],
                                   thousands='.', converters={'JN - Ano': np.int32, 'Total': np.int32})
        df_rint_1g.insert(0, 'instance', '1')

        df_rint_2g = pd.read_excel("painelcnj/indicadores/Rint-2g.xlsx", usecols=['JN - Ano', 'Total'],
                                   thousands='.', converters={'JN - Ano': np.int32, 'Total': np.int32})
        df_rint_2g.insert(0, 'instance', '2')

        df_rint_3g = pd.read_excel("painelcnj/indicadores/Rint-3g.xlsx", usecols=['JN - Ano', 'Total'],
                                   thousands='.', converters={'JN - Ano': np.int32, 'Total': np.int32})
        df_rint_3g.insert(0, 'instance', '3')

        df_rint = pd.concat([df_rint_1g, df_rint_2g, df_rint_3g])
        df_rint.rename(columns={"Total": "internal_appeal", "JN - Ano": "year"}, inplace=True)
        df_rint.set_index(['instance', 'year'], inplace=True)

        # internal appeals judged
        df_rintj_1g = pd.read_excel("painelcnj/indicadores/RintJ-1g.xlsx", usecols=['JN - Ano', 'Total'],
                                   thousands='.', converters={'JN - Ano': np.int32, 'Total': np.int32})
        df_rintj_1g.insert(0, 'instance', '1')

        df_rintj_2g = pd.read_excel("painelcnj/indicadores/RintJ-2g.xlsx", usecols=['JN - Ano', 'Total'],
                                   thousands='.', converters={'JN - Ano': np.int32, 'Total': np.int32})
        df_rintj_2g.insert(0, 'instance', '2')

        df_rintj_3g = pd.read_excel("painelcnj/indicadores/RintJ-3g.xlsx", usecols=['JN - Ano', 'Total'],
                                   thousands='.', converters={'JN - Ano': np.int32, 'Total': np.int32})
        df_rintj_3g.insert(0, 'instance', '3')

        df_rintj = pd.concat([df_rintj_1g, df_rintj_2g, df_rintj_3g])
        df_rintj.rename(columns={"Total": "internal_appeals_judged", "JN - Ano": "year"}, inplace=True)
        df_rintj.set_index(['instance', 'year'], inplace=True)

        # pendent internal appeals
        df_rintp_1g = pd.read_excel("painelcnj/indicadores/Rintp-1g.xlsx", usecols=['JN - Ano', 'Total'],
                                   thousands='.', converters={'JN - Ano': np.int32, 'Total': np.int32})
        df_rintp_1g.insert(0, 'instance', '1')

        df_rintp_2g = pd.read_excel("painelcnj/indicadores/Rintp-2g.xlsx", usecols=['JN - Ano', 'Total'],
                                   thousands='.', converters={'JN - Ano': np.int32, 'Total': np.int32})
        df_rintp_2g.insert(0, 'instance', '2')

        df_rintp_3g = pd.read_excel("painelcnj/indicadores/Rintp-3g.xlsx", usecols=['JN - Ano', 'Total'],
                                   thousands='.', converters={'JN - Ano': np.int32, 'Total': np.int32})
        df_rintp_3g.insert(0, 'instance', '3')

        df_rintp = pd.concat([df_rintp_1g, df_rintp_2g, df_rintp_3g])
        df_rintp.rename(columns={"Total": "internal_appeals_pendent", "JN - Ano": "year"}, inplace=True)
        df_rintp.set_index(['instance', 'year'], inplace=True)

        # Merge Datasets
        df_result = pd.merge(df_rint, df_rintj,  how="outer", on=["instance", "year"])
        df_result = df_result.merge(df_rintp,  how="outer", on=["instance", "year"])
        # df_result = df_result.fillna(-1)

        return df_result

    def loadHumanResources(self):
        """Class method to load indicator data related to human resources from CSV files.

        Returns:
            pandas.DataFrame: data from indicators related to human resources of all instances of jurisdiction of
                              the Brazilian electoral justice.
        """

        # magistrates
        df_mag_1g = pd.read_excel("painelcnj/indicadores/Mag-1g.xlsx", usecols=['JN - Ano', 'Total'],
                                   thousands='.', converters={'JN - Ano': np.int32, 'Total': np.int32})
        df_mag_1g.insert(0, 'instance', '1')

        df_mag_2g = pd.read_excel("painelcnj/indicadores/Mag-2g.xlsx", usecols=['JN - Ano', 'Total'],
                                   thousands='.', converters={'JN - Ano': np.int32, 'Total': np.int32})
        df_mag_2g.insert(0, 'instance', '2')

        df_mag_3g = pd.read_excel("painelcnj/indicadores/Mag-3g.xlsx", usecols=['JN - Ano', 'Total'],
                                   thousands='.', converters={'JN - Ano': np.int32, 'Total': np.int32})
        df_mag_3g.insert(0, 'instance', '3')

        df_mag = pd.concat([df_mag_1g, df_mag_2g, df_mag_3g])
        df_mag.rename(columns={"Total": "magistrates", "JN - Ano": "year"}, inplace=True)
        df_mag.set_index(['instance', 'year'], inplace=True)

        # public servants who work directly in judicial activities in lawsuits
        df_sajud_1g = pd.read_excel("painelcnj/indicadores/SaJud-1g.xlsx", usecols=['JN - Ano', 'Total'],
                                   thousands='.', converters={'JN - Ano': np.int32, 'Total': np.int32})
        df_sajud_1g.insert(0, 'instance', '1')

        df_sajud_2g = pd.read_excel("painelcnj/indicadores/SaJud-2g.xlsx", usecols=['JN - Ano', 'Total'],
                                   thousands='.', converters={'JN - Ano': np.int32, 'Total': np.int32})
        df_sajud_2g.insert(0, 'instance', '2')

        df_sajud_3g = pd.read_excel("painelcnj/indicadores/SaJud-3g.xlsx", usecols=['JN - Ano', 'Total'],
                                   thousands='.', converters={'JN - Ano': np.int32, 'Total': np.int32})
        df_sajud_3g.insert(0, 'instance', '3')

        df_sajud = pd.concat([df_sajud_1g, df_sajud_2g, df_sajud_3g])
        df_sajud.rename(columns={"Total": "judiciary_civil_servants", "JN - Ano": "year"}, inplace=True)
        df_sajud.set_index(['instance', 'year'], inplace=True)

        # Merge Datasets
        df_result = pd.merge(df_mag, df_sajud,  how="outer", on=["instance", "year"])
        # df_result = df_result.fillna(-1)

        return df_result


if __name__ == "__main__":
    EJNumbers = JusticeNumbers()
    ejNewCases = EJNumbers.loadNewCases()
    ejInternalAppeals = EJNumbers.loadInternalAppeals()
    ejHR = EJNumbers.loadHumanResources()


    ejJusticeNumbers = pd.merge(ejNewCases, ejInternalAppeals, how="outer", on=["instance", "year"])
    ejJusticeNumbers = ejJusticeNumbers.merge(ejHR, how="outer", on=["instance", "year"])
    ejJusticeNumbers.sort_values(by=['instance', 'year'], ascending=True, inplace=True)
    # df = df.fillna(-1)

    # By using a loop to convert float into int
    for col in ejJusticeNumbers.columns:
        if ejJusticeNumbers[col].dtype == 'float64':
            ejJusticeNumbers[col] = ejJusticeNumbers[col].astype('Int64')

    # print(df)

    ejJusticeNumbers.to_csv('br_electoral_JusticeNumbers.csv')
