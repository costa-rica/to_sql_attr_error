from models02 import engine, Apple_health_export
import pandas as pd

dataset = {'id': [1], 'creationDate':['2022-10-15'], 'value':['5']}

df=pd.DataFrame(data=dataset)

# Here is the problem
df.to_sql('Apple_health_export', engine, if_exists='append', index=False)

# replacing this line with the lowercase 'apple_health_export' solves the problem
# this needs to match what i have in models02.py: __tablename__ = 'apple_health_export'
# df.to_sql('apple_health_export', engine, if_exists='append', index=False)