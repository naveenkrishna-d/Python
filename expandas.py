import pandas as pd

data = {
    'Name': ['Alice','Bob','Charlie'],
    'Age':[25,30,35],
    'City':['New york','LA','Chicago']
}

df=pd.DataFrame(data)

# print("DataFrame:\n",df)
# print("Column names:",df.columns)
# print("Data types:\n",df.dtypes)

# print("select 'name' column:\n", df['Name'])
#print("select rows where age>25:\n",df['Age']>25)

#add new column
df['Salary']=[7000,8000,9000]

#handling missing values
df.loc[3] = ['David',None,'San Jose', None]

print(f"with missing values\n{df}")
print(f"drop rows with missing values:\n{df.dropna()}")
print("fill missing values:\n",df.fillna(0))