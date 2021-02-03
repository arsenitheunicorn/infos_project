import pandas as pd

def main():
    df_q = pd.read_excel(
        'test_queries.xlsx',
        usecols="B,C,G"
    )

    df_a = pd.read_excel('db_default\\answers_base.xlsx')

    df = df_q.merge(df_a, on='Номер связки', how='left')

    df[["Текст вопроса", "Номер связки", 'lemmas', "Текст ответа"]].to_excel('final_db.xlsx', index=False)

if __name__ == "__main__":
    main()