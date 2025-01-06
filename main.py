import pandas as pd
import matplotlib.pyplot as plt

from src.functions.cleaner import *
from src.functions.descriptive_statistics import *
from src.functions.seats_entry_2022 import *

from src.values.cinemas_columns import *

def get_seats_diagram(seat) :
    seats_df = pd.DataFrame(seat)
    seats_df.set_index(seat.index)[
        ["entrée_moyenne"]].plot(kind='bar', figsize=(12, 6))
    plt.table('Entrées moyenne par fauteuils dans les salles de cinémas')
    plt.ylabel('entrée_moyenne')
    plt.xlabel('commune')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.legend(title="Légende")
    plt.show()


cinemas_file = get_clean_data('data/cinemas.csv') # Nettoyage des données

cinemas_filt_columns = get_right_colunms(cinemas_file, cinemas_columns) # Récupération des données qui nous intéressent

cinemas_data = cinemas_filt_columns

#Calcul de la moyenne et de l'écart-type des colonnes sélectionnées
cinemas_means = get_means(cinemas_data, cinemas_columns_means)
cinemas_std = get_std(cinemas_data, cinemas_columns_means)

# cinemas_entry_per_seat = get_entry_per_seats_2022(cinemas_data)

average = cinemas_data["entrées 2022"] / cinemas_data["fauteuils"]
tab =[]
for el in average:
    tab.append(el)

cinemas_data.insert(loc=7, column="entry_seats_2022", value=tab)

# print(cinemas_data.groupby("commune").agg(
#     entrée_moyenne=("entry_seats_2022", "mean")
# ))

# print(cinemas_data.groupby("commune").agg(
#     entrée_moyenne=("entry_seats_2022", "mean")
# ).sort_values(by='entrée_moyenne', ascending=False).head(3))

# print(cinemas_data.groupby("commune").agg(
#     entrée_moyenne=("entry_seats_2022", "mean")
# ).sort_values(by='entrée_moyenne', ascending=True).head(3))


cinemas_seats_data = cinemas_data.groupby("commune").agg(
    entrée_moyenne=("entry_seats_2022", "mean")
).sort_values(by='entrée_moyenne', ascending=False).head(10)

# print(cinemas_data)
print(cinemas_seats_data)
# print(cinemas_seats_data.index)

get_seats_diagram(cinemas_seats_data)

# print(cinemas_data.head())
# print('\n --- \n')
# print(cinemas_means)
# print(cinemas_std)
# print('\n --- \n')
# print(cinemas_entry_per_seat)