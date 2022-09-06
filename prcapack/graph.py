import pandas as pd
import matplotlib.pyplot as plt

def graphs():

    df = pd.DataFrame({'mass': [0.330, 4.87, 5.97],
                       'radius': [2439.7, 6051.8, 6378.1]},
                      index=['Mercury', 'Venus', 'Earth'])
    plot = df.plot.pie(y='mass', figsize=(5, 5))

    img1=plt.savefig("C:/Users/922619/PycharmProjects/sqlconection/prac/ab.png")



graphs()
