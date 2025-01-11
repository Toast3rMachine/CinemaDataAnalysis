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