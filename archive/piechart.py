import pandas as pd

import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("titles.csv")
# data.groupby("type")["id"].count().plot.pie()
# data[data.type == 'SHOW'].age_certification.groupby("age_certification").count   .plot.pie()
#data.groupby('type')['age_certification'].count().plot.pie()
data[data.type == 'SHOW'].groupby("age_certification", dropna=False).id.count().plot.pie(autopct='%1. f2%%')
plt.show()