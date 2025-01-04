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

cinemas_file = get_clean_data('data/cinemas.csv')
cinemas_columns = [
    'commune',
    'population de la commune',
    'écrans',
    'fauteuils',
    'entrées 2021',
    'entrées 2022',
    'AE'
]
# On garde ces valeurs car ce sont les plus intéressantes.
# La nom et la population de la commune sont des données importantes sur la localisation et le nombre de visiteurs potentiels.
# 'AE' nous permet de savoir si le cinéma est classé Art & Essai.
# Enfin, le reste des colonnes sont celles qui nous permettront d'effectuer notre étude. 

cinemas_filt_columns = get_right_colunms(cinemas_file, cinemas_columns)

print(cinemas_filt_columns)