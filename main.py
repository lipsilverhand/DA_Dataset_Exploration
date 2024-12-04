import pandas as pd

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m1_survey_data.csv"

df = pd.read_csv(url)

print(df.head())

num_rows = df.shape[0]
print(f'Number of rows: {num_rows}')


num_cols = df.shape[1]
print(f'Number of columns: {num_cols}')

print(df.dtypes) #data types

mean_age = df['Age'].mean()
print(f'Mean of age: {mean_age}')

unique_countries = df['Country'].nunique()
print(f"Number of unique countries: {unique_countries}")