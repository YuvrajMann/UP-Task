# Pandas import
import pandas as pd

# Reading the csv and getting dataframe
df = pd.read_csv(r'./Titanic.csv')

# Task 1 - Prints a count of missing data for each column

# Ietaring all columns
for col in df.columns:
    #Priniting the column name and not null fields sum for each column
    print(f'{col} - {df[col].isna().sum()}')

# Task 2 - Prints average age of all the people who survived

# Getting dataframe where person survived
rslt_df = df.loc[df['Survived'] ==1]

# Getting rows where age is not null
age_na_df=rslt_df.loc[rslt_df['Age'].notnull()]

# Getting mean of not null fields of processed dataframe
age_na_df['Age'].mean()
