import pandas as pd
import numpy as np

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
varExp = ['écrans', 'fauteuils', 'population de la commune']
varTar2021 = ['entrées 2021']
varTar2022 = ['entrées 2022']

varExp = get_right_colunms(cinemas_data, varExp)
varTar2021 = get_right_colunms(cinemas_data, varTar2021)
varTar2022 = get_right_colunms(cinemas_data, varTar2022)

# print(varExp)
# print(varTar2021)
# print(varTar2021.corr())

# print(cinemas_data[cinemas_data['entrées 2021'] != 0]) 
df = pd.DataFrame(cinemas_data[cinemas_data['entrées 2021'] != 0])
# df['croissance'] = (
#     (df['entrées 2022'] - df['entrées 2021']) / df['entrées 2021']
# )

# df['entrées 2023 (estimé)'] = (
#     df['entrées 2022'] * (1+df['croissance'])
# )

# x = df[['entrées 2022', 'croissance']]
# print(x)
# y = df[['entrées 2023 (estimé)']]

# model = LinearRegression()
# model.fit(x,y)

# print("Coef : ", model.coef_)
# print("Intercept : ", model.intercept_)

# df["Prédiction 2023"] = model.predict(x)
# print(df[["commune","Prédiction 2023"]])

Y = df['entrées 2022']
X = df[['écrans', 'fauteuils', 'population de la commune']]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state=101)
print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)
print(Y_test.shape)

print("Coef de détermination : ", r2_score(X_train.shape, X_test.shape))
# print(r2_score(Y_train.shape, Y_test.shape))

print("Erreur moyenne absolue : ", mean_absolute_error(X_train.shape, X_test.shape))
# print(mean_absolute_error(Y_train.shape, Y_test.shape))