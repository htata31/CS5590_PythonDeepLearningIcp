import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt


plt.style.use(style='ggplot')
plt.rcParams['figure.figsize'] = (10, 6)

train = pd.read_csv(Path('Dataset1/train.csv'))

train.SalePrice.describe()

# scatter plot between Garage
print(train[['GarageArea']])
plt.scatter(train.GarageArea, train.SalePrice, alpha=.75, color='r')
plt.show()

_filter = train[(train.GarageArea < 1000) & (train.GarageArea > 200)]
plt.scatter(_filter.GarageArea, _filter.SalePrice, alpha=.75, color='b')
plt.show()
