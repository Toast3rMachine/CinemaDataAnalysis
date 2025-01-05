import pandas as pd
import matplotlib.pyplot as plt

from src.functions.cleaner import *
from src.functions.descriptive_statistics import *

from src.values.cinemas_columns import *

cinemas_file = get_clean_data('data/cinemas.csv') # Nettoyage des données

cinemas_filt_columns = get_right_colunms(cinemas_file, cinemas_columns) # Récupération des données qui nous intéressent

cinemas_data = cinemas_filt_columns

#Calcul de la moyenne et de l'écart-type des colonnes sélectionnées
cinemas_means = get_means(cinemas_data, cinemas_columns_means)
cinemas_std = get_std(cinemas_data, cinemas_columns_means)

print(cinemas_data.head())
print(cinemas_means)
print(cinemas_std)