# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import os
os.system('cls')
import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

def one_hot(data, columns='whoAmI'):
  df = pd.DataFrame({columns:data[columns],'temp': [1]* len(data)})
  return pd.pivot_table(data=df, index=data.index, columns=df[columns], fill_value=0).droplevel(0, axis=1).rename_axis('', axis=1)

data.head()
# print (one_hot(data))