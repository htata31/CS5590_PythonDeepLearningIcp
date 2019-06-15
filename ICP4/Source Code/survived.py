import pandas as pd
from pathlib import Path

train_df = pd.read_csv(Path('Dataset1/train.csv'))
x = train_df[["Sex", "Survived"]].groupby(['Sex'], as_index=False).mean().sort_values(by='Survived', ascending=False)
print(x)






