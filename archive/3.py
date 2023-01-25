import pandas as pd

import matplotlib.pyplot as plt
import numpy as np
# open.dataframe() view
data = pd.read_csv("titles.csv")

d2 = data[data.release_year >= 2000]
d3 = d2[data['imdb_score'] > 8.0]

d3.groupby('release_year')['imdb_score'].count().plot.bar()
# plt.title('IMDB scores of movies and shows')
# plt.xlabel('IMDB score')
# plt.ylabel('Quantity of movies and shows')
plt.show()