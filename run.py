from models02 import engine, Apple_health_export
import pandas as pd

dataset = {'id': [1], 'creationDate':['2022-10-15'], 'value':['5']}

df=pd.DataFrame(data=dataset)
df.to_sql('apple_health_export', engine, if_exists='append', index=False)