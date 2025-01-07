import pandas as pd
import matplotlib.pyplot as plt

def get_entry_per_seats_2022(df, columns, ascending=False, head=3):
    average = df[columns[2]] / df[columns[1]]
    tab =[]
    for el in average:
        tab.append(el)

    if "entry_seats_2022" not in df.columns:
        df.insert(loc=7, column="entry_seats_2022", value=tab)

    entry_per_seat = df.groupby(columns[0]).agg(
            entrée_moyenne=("entry_seats_2022", "mean")
        ).sort_values(by='entrée_moyenne', ascending=ascending).head(head)

    return entry_per_seat

def get_seats_diagram(df, columns) :
    df = get_entry_per_seats_2022(df, columns, head=10)
    seats_df = pd.DataFrame(df)
    seats_df.set_index(df.index)[
        ["entrée_moyenne"]].plot(kind='bar', figsize=(12, 6))
    plt.table('Entrées moyenne par fauteuils dans les salles de cinémas')
    plt.ylabel('entrée_moyenne')
    plt.xlabel('commune')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.legend(title="Légende")
    plt.show()