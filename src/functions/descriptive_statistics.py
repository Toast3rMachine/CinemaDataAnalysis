def get_means(df, columns):
    mean = ''
    for col in columns:
        mean += 'La moyenne de la colonne ' + col + ' est ' + str(int(df[col].mean())) + '\n'
    return mean

def get_std(df, columns):
    mean = ''
    for col in columns:
        mean += 'L\'écart-type de la colonne ' + col + ' est ' + str(int(df[col].std())) + '\n'
    return mean