import matplotlib.pyplot as plt
import pandas as pd

from src.functions.cleaner import get_right_colunms

def get_scatter_graph(df, columns, coefCorr):
    df = get_right_colunms(df, columns)
    scatter_df = pd.DataFrame(df)
    scatter_df.set_index(df.index)[
        [columns[0], columns[1]]].plot(
            kind='scatter',x=columns[1], y=columns[0])
    
    avgX = df[columns[1]].mean()
    avgY = df[columns[0]].mean()
    
    sumX = 0
    sumY = 0
    sumXY = 0

    # for x in df[columns[1]]:
    #     sumX += (avgX-x)**2
    # for y in df[columns[0]]:
    #     sumY += (avgY-y)**2

    for x,y in zip(df[columns[1]], df[columns[0]]):
        sumX += (avgX-x)**2
        sumY += (avgY-y)**2
        sumXY += (avgX-x)*(avgY-y)

    # sumXY = sumX * sumY
    b = sumXY / sumX
    a = avgY - b*avgX

    print(coefCorr, a, b, avgY, sumXY)

    plt.plot(y , a+b*x , color='r')
    plt.table('Nuage de points + Régression Linéaire')
    # plt.axis(ymin=0, ymax=30)
    plt.ylabel('Nombres ' + columns[0])
    plt.xlabel('Nombre d\'entrées en 2022')
    plt.show()
