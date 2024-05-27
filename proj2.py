#Lis moun yo
"""
A.	Badio Marklens
B.	Nelson Benito
C.	Hector Wendel
D.	Badio Wilkens
E.	Ovide Samuel
F.	Payen Sterlin Myfedjy
G.	Pierre Louis Naika
"""

import pandas as pd

file_path = 'company.csv'
df = pd.read_csv(file_path)

df['salary'] = df['salary'].str.upper()

def convert_salary(salary):
    if pd.isna(salary):
        return salary
    salary = salary.upper().replace(',', '') 
    if 'K' in salary:
        return float(salary.replace('K', '')) * 1000
    return float(salary)

df['salary'] = df['salary'].apply(convert_salary)
df['salary'] = df['salary'].astype('Float64')

df.dropna(inplace=True)

df['salary'] = pd.to_numeric(df['salary'], errors='coerce')

df['years_at_company'] = df['years_at_company'].str.replace(r'\D+', '', regex=True)

df['gender'] = df['gender'].str.upper()
df['gender'] = df['gender'].replace({'MALE': 'M', 'FEMALE': 'F'})

df['hired_date_1'] = pd.to_datetime(df['hired_date'], format='%d-%b-%y', errors='coerce')
df['hired_date_2'] = pd.to_datetime(df['hired_date'], format='%d-%b-%Y', errors='coerce')
df['hired_date_3'] = pd.to_datetime(df['hired_date'], format='%d-%m-%Y', errors='coerce')
df['hired_date_4'] = pd.to_datetime(df['hired_date'], format='%d-%m-%y', errors='coerce')

df['hired_date'] = df['hired_date_1'].combine_first(df['hired_date_2']).combine_first(df['hired_date_3']).combine_first(df['hired_date_4'])

df.drop(columns=['hired_date_1', 'hired_date_2', 'hired_date_3', 'hired_date_4'], inplace=True)

df['hired_date'] = df['hired_date'].dt.strftime('%d-%m-%Y')


df['age'] = pd.to_numeric(df['age'], errors='coerce')
df['job_satisfaction'] = pd.to_numeric(df['job_satisfaction'], errors='coerce')
df['performance_score'] = pd.to_numeric(df['performance_score'], errors='coerce')
df['last_promotion_year'] = pd.to_numeric(df['last_promotion_year'], errors='coerce')

repatisyon_depatman = df['department'].value_counts()

repatisyon_seks_depatman = df.groupby(['department', 'gender']).size()

laj_mwayen_anplaye = df.groupby('department')['age'].mean()

sale_mwayenn = df.groupby('department')['salary'].mean()

satisfaksyon_travay = df.groupby('department')['job_satisfaction'].mean()

ane_kouran = pd.to_datetime('today').year
df['ane_dpi_denye_pwomosyon'] = ane_kouran - df['last_promotion_year']

mwayenn_tan_pwomosyon = df.groupby('department')['ane_dpi_denye_pwomosyon'].mean()

mwayenn_sale = df.groupby('education_level')['salary'].mean()







