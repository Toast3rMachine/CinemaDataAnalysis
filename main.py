from src.functions.cleaner import *
from src.functions.descriptive_statistics import *
from src.functions.seats_entry_2022 import *

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
print(cinemas_data_corr.head())
print('\n --- \n')
print(cinemas_data_corr[['écrans','fauteuils','entrées 2022']].corr(method='pearson', numeric_only=True))