import pandas as pd

import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("titles.csv")
# data.groupby("type")["id"].count().plot.pie()
# SHOWS = data.type
# data.groupby('type')['age_certification'].count().plot.pie()
# data[data.type == 'SHOW']["imdb_score"].hist()
# data[data.type == 'MOVIE']["imdb_score"].hist()

data.groupby('type')['imdb_score'].hist(bins=50)
plt.title('IMDB scores of movies and shows')
plt.xlabel('IMDB score')
plt.ylabel('Quantity of movies and shows')

# np.arange(start=0, stop=10, step=0.2)
plt.show()

# data = pd.read_csv("titles.csv")
pass
