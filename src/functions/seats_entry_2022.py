def get_entry_per_seats_2022(df):
    mean = ''
    for el in df["commune"]:
        line = df[df["commune"] == el]
        df["entrées 2022", "fauteuils"]
        division = str((line["entrées 2022"] / line["fauteuils"]))
        mean += "Les entrées moyenne par fauteuil de la region " + el + " est d'environ : " + division + "\n"
    return mean