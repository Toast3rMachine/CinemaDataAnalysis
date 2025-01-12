import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

from src.functions.cleaner import *
from src.functions.descriptive_statistics import *
from src.functions.seats_entry_2022 import *
from src.functions.correlation import *

from src.values.cinemas_columns import *


cinemas_file = get_clean_data('data/cinemas.csv') # Nettoyage des données

cinemas_filt_columns = get_right_colunms(cinemas_file, cinemas_columns) # Récupération des données qui nous intéressent
cinemas_corr_filt_columns = get_right_colunms(cinemas_file, cinemas_columns_corr)

cinemas_data = cinemas_filt_columns
cinemas_data_corr = cinemas_corr_filt_columns

#Calcul de la moyenne et de l'écart-type des colonnes sélectionnées
cinemas_means = get_means(cinemas_data, cinemas_columns_means)
cinemas_std = get_std(cinemas_data, cinemas_columns_means)

#EXO 1
# print(cinemas_data.head())
# print('\n --- \n')
# print(cinemas_means)
# print(cinemas_std)
# print('\n --- \n')

#EXO 2
# print(get_entry_per_seats_2022(cinemas_data, cinemas_columns_entry_per_seats))
# print(get_entry_per_seats_2022(cinemas_data, cinemas_columns_entry_per_seats, True))
# get_seats_diagram(cinemas_data, cinemas_columns_entry_per_seats)

#EXO 3
# print(cinemas_data_corr.head())
# print('\n --- \n')
# corr_Encran = cinemas_data_corr[['écrans','entrées 2022']].corr(method='pearson', numeric_only=True)
# coef_Corr_Ecran = corr_Encran['entrées 2022'].values[0]

# print(corr_Encran)
# print('\n')
# print(coef_Corr_Ecran)

# print(cinemas_data_corr[['fauteuils','entrées 2022']].corr(method='pearson', numeric_only=True))
# get_scatter_graph(cinemas_data, ['écrans','entrées 2022'], coef_Corr_Ecran)
# get_scatter_graph(cinemas_data_corr, ['fauteuils','entrées 2022'])

#EXO 4
#On retire les cinémas qui n'ont pas fait d'entrées en 2021
# df = pd.DataFrame(cinemas_data[cinemas_data['entrées 2021'] != 0])

# X = df[['écrans', 'fauteuils', 'population de la commune']]
# Y = df[['entrées 2021']]

# model = LinearRegression()
# model.fit(X,Y)
# Intercept = model.intercept_
# Coef = model.coef_
# Score = model.score(X,Y)

# print(Intercept, Coef, Score)

# df[['entrées 2023']] = model.predict(X)
# print(df[['commune', 'entrées 2023']])

#Split train/test
# X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state=101)
# print(X_train.shape)
# print(X_test.shape)
# print(Y_train.shape)
# print(Y_test.shape)

# print("Coef de détermination : ", r2_score(X_train.shape, X_test.shape))

# print("Erreur moyenne absolue : ", mean_absolute_error(X_train.shape, X_test.shape))

#Les prédictions ne correspondent pas aux valeurs réelles