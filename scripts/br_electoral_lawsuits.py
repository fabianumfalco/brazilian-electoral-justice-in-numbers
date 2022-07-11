import pandas as pd
import numpy as np


def cno():
    df_cn_tse = pd.read_excel("../painelcnj/gestao-judiciaria/Novos-TSE.xlsx")
    df_cn_tre = pd.read_excel("../painelcnj/gestao-judiciaria/Novos-TRE.xlsx")
    df_cn_je = pd.concat([df_cn_tse, df_cn_tre])
    df_cn_je = df_cn_je.rename(
        columns={"Valor": "new_lawsuit", "JN - Ano": "year", "Variáveis JN - Nível 1": "level_jurisdiction"})
    df_cn_je['level_jurisdiction'] = df_cn_je['level_jurisdiction'].replace(['Tribunal superior','2º grau', '1º grau'], ['3', '2', '1'])
    # df_cn_je = df_cn_je.iloc[:, [1, 0,2]]
    df_cn_je.set_index(['year', 'level_jurisdiction'], inplace = True)
    #df_cn_je = df_cn_je.sort_index(0)
    return df_cn_je

def rint():
    df_rint_ze = pd.read_excel("../painelcnj/indicadores/RintC1g.xlsx", usecols=['JN - Ano', 'Total'],
                               thousands='.', converters={'JN - Ano':str,'Total':np.int32})
    df_rint_ze.rename(columns={"Total": "internal_appeal", "JN - Ano": "year"}, inplace=True)
    df_rint_ze.insert(1, 'level_jurisdiction', '1')

    df_rint_tre = pd.read_excel("../painelcnj/indicadores/Rint2g-TRE.xlsx", usecols=['JN - Ano', 'Total'],
                                thousands='.', converters={'JN - Ano': str, 'Total': np.int32})
    df_rint_tre.rename(columns={"Total": "internal_appeal", "JN - Ano": "year"}, inplace=True)
    df_rint_tre.insert(1, 'level_jurisdiction', '2')

    df_rint_tse = pd.read_excel("../painelcnj/indicadores/Rint-TSE.xlsx", usecols=['JN - Ano', 'Total'],
                                thousands='.', converters={'JN - Ano': str, 'Total': np.int32})
    df_rint_tse.rename(columns={"Total": "internal_appeal", "JN - Ano": "year"}, inplace=True)
    df_rint_tse.insert(1, 'level_jurisdiction', '3')

    df_rint = pd.concat([df_rint_ze, df_rint_tre, df_rint_tse])

    df_rint.set_index(['year', 'level_jurisdiction'], inplace=True)

    return df_rint


def main():

    df1 = cno()
    # print(df1)
    # print("=======")
    df2 = rint()
    # print(df2)

    df3 = df1.merge(df2, on=['year', 'level_jurisdiction'], how='outer')
    # df3 = df1.merge(df2, on=['year', 'level_jurisdiction'])

    #df = pd.concat([df1, df2])

    # df.to_csv("br_electoral_lawsuits.csv")
    print(df)

if __name__ == "__main__":
    main()
