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
# print('Moyenne des colonnes')
# print(cinemas_means)
# print('Ecart-type des colonnes')
# print(cinemas_std)
# print('\n --- \n')

#EXO 2
# print('Les trois régions ayant les meilleurs résultats')
# print('\n --- \n')
# print(get_entry_per_seats_2022(cinemas_data, cinemas_columns_entry_per_seats))
# print('\n')
# print('Les trois régions ayant les pires résultats')
# print('\n --- \n')
# print(get_entry_per_seats_2022(cinemas_data, cinemas_columns_entry_per_seats, True))
# get_seats_diagram(cinemas_data, cinemas_columns_entry_per_seats)

#EXO 3
# print(cinemas_data_corr.head())
# print('\n --- \n')
# corr_Encran = cinemas_data_corr[['écrans','entrées 2022']].corr(method='pearson', numeric_only=True)
# corr_Fauteuil = cinemas_data_corr[['fauteuils','entrées 2022']].corr(method='pearson', numeric_only=True)

# print('\n')
# print('Corrélation entre les écrans et les entrées de 2022')
# print(corr_Encran)
# print('\n')
# print('Corrélation entre les fauteuils et les entrées de 2022')
# print(corr_Fauteuil)

# get_scatter_graph(cinemas_data, ['écrans','entrées 2022'])
# get_scatter_graph(cinemas_data, ['fauteuils','entrées 2022'])

#EXO 4
# df = pd.DataFrame(cinemas_data[cinemas_data['entrées 2021'] != 0]) #On retire les cinémas qui n'ont pas fait d'entrées en 2021

# X = df[['écrans', 'fauteuils', 'population de la commune']]
# Y = df[['entrées 2021']]

# model = LinearRegression()
# model.fit(X,Y)
# Intercept = model.intercept_
# Coef = model.coef_
# Score = model.score(X,Y)

# print('Ordonnée à l\'origine, coefficients et coefficent de détermination')
# print(Intercept, Coef, Score)

# df[['entrées 2022']] = model.predict(X)
# print('\n')
# print('Prédictions des entrées pour 2022')
# print(df[['commune', 'entrées 2022']])

# X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state=101) #Split train/test
# print('\n')
# print('Résultat du train/test (80%/20%)')
# print(X_train.shape)
# print(X_test.shape)
# print(Y_train.shape)
# print(Y_test.shape)

# print("Coef de détermination : ", r2_score(X_train.shape, X_test.shape))

# print("Erreur moyenne absolue : ", mean_absolute_error(X_train.shape, X_test.shape))

# print('\n') #Les prédictions pour 2022 ne correspondent pas aux valeurs réelles de 2022, on a même des valeurs négatives dans nos prédictions
# print('Prédictions des entrées pour 2022 (10 premières lignes)')
# print(df[['commune', 'entrées 2022']].head(10))
# print('\n')
# print('Valeurs réelles des entrées de 2022 (10 premières lignes)')
# print(cinemas_data[['commune', 'entrées 2022']].head(10))