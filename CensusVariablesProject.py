import codecademylib3

# Import pandas with alias
import pandas as pd

# Read in the census dataframe
census = pd.read_csv('census_data.csv', index_col=0)

# Viewing the first 5 rows of the df
print(census.head())

# Checking the data types of each variable
print(census.dtypes)

# Print unique values of the birth_year 
print(census.birth_year.unique())

# replacing missing value with 1967 (confirmed after research)
census['birth_year'] = census['birth_year'].replace(['missing'], 1967)
print(census.birth_year.unique())

# Changing the datatype from string to int, and confirm changes with 'dtypes'
census['birth_year'] = census['birth_year'].astype(int)
print(census.dtypes)

# The average birth year of census respondents
print(census['birth_year'].mean())

# Converting 'higher_tax' variable to category datatype
census['higher_tax'] = pd.Categorical(census['higher_tax'], ['strongly disagree','disagree','neutral','agree','strongly agree'], ordered = True)
print(census['higher_tax'].unique())

# Label encoding the 'higher_tax' variable
census['higher_tax_encoded'] = census['higher_tax'].cat.codes
print(census.head())
print(census.higher_tax_encoded.median())

# One-Hot-Encode the 'marital_status' variable
census_new = pd.get_dummies(data=census, columns= ['marital_status'])
print(census.head())

# Create new variable 'marital_codes' by Label Encoding the marital_status
census['marital_status'] = pd.Categorical(census['marital_status'],['divorces','married','single','widowed'],ordered=True)
census['marital_codes'] = census['marital_status'].cat.codes
print(census)

# Creation of new variable 'age_group' based on birth year with 5 year increments.
five_hold = list(range(1940, 2011, 5))
print(five_hold)
census['age_group'] = pd.cut(census.birth_year, five_hold)
census['age_group_codes'] = census.age_group.cat.codes
print(census)