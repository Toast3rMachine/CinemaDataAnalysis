import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

from src.functions.cleaner import get_right_colunms

def get_scatter_graph(df, columns):
    df = get_right_colunms(df, columns)
    scatter_df = pd.DataFrame(df)
    scatter_df.set_index(df.index)[
        [columns[0], columns[1]]].plot(
            kind='scatter',x=columns[1], y=columns[0])
    
    # X = df[[columns[0]]]
    # Y = df[[columns[1]]]
    
    # model = LinearRegression()
    # model.fit(X,Y)
    # Intercept = model.intercept_ #Ordonée à l'origine
    # Coef = model.coef_ #Coefficient directeur

    plt.table('Nuage de points + Régression Linéaire')
    # plt.plot(X, Intercept + Coef * X, color='red') #Courbe de régression linéaire
    # plt.axis(ymin=0, ymax=30)
    plt.ylabel('Nombres ' + columns[0])
    plt.xlabel('Nombre d\'entrées en 2022')
    plt.show()
