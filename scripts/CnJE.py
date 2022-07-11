import pandas as pd


def main():
    df_cn_tse = pd.read_excel("../painelcnj/gestao-judiciaria/Novos-TSE.xlsx")
    df_cn_tre = pd.read_excel("../painelcnj/gestao-judiciaria/Novos-TRE.xlsx")
    df_cn_je = pd.concat([df_cn_tse, df_cn_tre])
    df_cn_je = df_cn_je.rename(
        columns={"Valor": "new_lawsuit", "JN - Ano": "year", "Variáveis JN - Nível 1": "level_jurisdiction"})
    df_cn_je['level_jurisdiction'] = df_cn_je['level_jurisdiction'].replace(['Tribunal superior','2º grau', '1º grau'], ['3', '2', '1'])
    # df_cn_je = df_cn_je.iloc[:, [1, 0,2]]
    df_cn_je.set_index(['year', 'level_jurisdiction'], inplace = True)
    #df_cn_je = df_cn_je.sort_index(0)

    df_cn_je.to_csv("electoral_judicial_management.csv")
    print(df_cn_je)


if __name__ == "__main__":
    main()
