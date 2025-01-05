import pandas as pd

def get_clean_data(data):
        return (pd.read_csv(data, sep=';', encoding='utf-8')
                .drop_duplicates()
                .fillna({'commune': '',
                        'population de la commune': 0,
                        'écrans': 0,
                        'fauteuils': 0,
                        'entrées 2021': 0,
                        'entrées 2022': 0,
                        'AE': ''})
                .astype({'population de la commune': int,
                        'écrans': int,
                        'fauteuils': int,
                        'entrées 2021': int,
                        'entrées 2022': int,})
                .assign(comunne=lambda x: x['commune'].str.strip())
                .assign(AE=lambda x: x['AE'].str.strip())
                )

def get_right_colunms(df, columns):
        missing_columns = [col for col in columns if col not in df.columns]
        if missing_columns:
                return pd.DataFrame()
        return df[columns]