
import pandas as pd
data = pd.read_csv(r'C:\Users\39338\Desktop\python-data-cleaning-master\Datasets\BL-Flickr-Images-Book.csv')
data.head()
data.shape[0]
data.shape[1]
data.dropna(subset=['Date of Publication'], axis = 0) 
data.shape[0]
to_drop = ['Edition Statement',
           'Corporate Author',
           'Corporate Contributors',
           'Former owner',
           'Engraver',
           'Contributors',
           'Issuance type',
           'Shelfmarks']
data.drop(to_drop, inplace = True, axis = 1) 
data.head()
data.dropna(axis=0,how='any')

data.set_index('Identifier', inplace = True)
data.head()

data.drop_duplicates(keep = 'first', inplace = True)

data['Date of Publication'].head(25)

df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
                  index=['cobra', 'viper', 'sidewinder'],
                  columns=['max_speed', 'shield'])
dop = str(df.loc['cobra'])