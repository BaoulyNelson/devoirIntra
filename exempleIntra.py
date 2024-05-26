"""
Pwojè an gwoup (7 moun maksimòm)
Objektif prensipal pwojè sa, se kreye yon koleksyon done ki byen prepare pou vizyalizasyon. Wap gen pou w itilize, netwaye, transfòme done sa yo ak libreri Python pandas ak numpy.

Sa vle di wap jere valè ki manke yo (NaN), detekte kolòn ki merite transfòme an lòt tip done, epi aplike analiz estatistik bazik oubyen avanse.

I) Kesyon sou Analiz Demografik
1.	Repatisyon chak anplwaye nan chak depatman.
2.	Repatisyon pa sèks nan chak depatman.
3.	Mwayèn laj anplwaye yo pou chak depatman.

II) Kesyon sou Salè
1.	Mwayèn salè nan chak depatman
2.	Satisfaksyon travay sou chak depatman

III) Kesyon sou Pwomosyon ak Edikasyon
1.	Ki mwayèn tan ki genyen depi dènye fwa konpayi a te bay yon pwomosyon nan chak depatman?
2.	Bay mwayèn salè ki ekziste an fonksyon de nivo edikasyon anplwaye yo (Bachelor, Master)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# annal cheche fichye a
df = pd.read_csv('company.csv')

# Verifye valeur ki manke yo
print(df.isnull().sum())

# Remplir les valeurs manquantes pour 'gender' par le mode (valeur la plus fréquente)
df['gender'] = df['gender'].fillna(df['gender'].mode()[0])

# nou konveti kolon hired_date en type datetime
df['hired_date'] = pd.to_datetime(df['hired_date'], format='%d-%m-%Y', errors='coerce')

# nou konveti 'salary' en format nimerik 
df['salary'] = df['salary'].replace(r'[\$,K]', '', regex=True).astype(float)

# nou konveti years_at_company en format nimerik
df['years_at_company'] = df['years_at_company'].replace(r'[^0-9]', '', regex=True).astype(float)

# nou verifye ak konveti lot kolon si sa nesese
df['age'] = pd.to_numeric(df['age'], errors='coerce')
df['job_satisfaction'] = pd.to_numeric(df['job_satisfaction'], errors='coerce')
df['performance_score'] = pd.to_numeric(df['performance_score'], errors='coerce')
df['last_promotion_year'] = pd.to_numeric(df['last_promotion_year'], errors='coerce')

# Remplir les valeurs manquantes pour 'salary' et 'education_level' par une méthode appropriée
df['salary'] = df['salary'].fillna(df['salary'].median())
df['education_level'] = df['education_level'].fillna('Unknown')

# nou reveriye tout enfomasyon yo apre konvesyon yo
# print(df.info())

# Ajoute 1 kolon ki rele years_since_last_promotion
current_year = pd.Timestamp.now().year
df['years_since_last_promotion'] = current_year - df['last_promotion_year']

#Repatisyon chak anplwaye nan chak depatman.
dept_distribution = df['department'].value_counts()
print(dept_distribution)

# graf pou Repatisyon chak anplwaye nan chak depatman.
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='department')
plt.title('Répartition de chaque employé dans chaque département')
plt.xlabel('Département')
plt.ylabel('Nombre d\'employés')
plt.show()

# Repatisyon pa sèks nan chak depatman.
gender_dept_distribution = df.groupby(['department', 'gender']).size().unstack()
print(gender_dept_distribution)

#graf pou Repatisyon pa sèks nan chak depatman.
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='department', hue='gender')
plt.title('Répartition par sexe dans chaque département')
plt.xlabel('Département')
plt.ylabel('Nombre d\'employés')
plt.show()

# Mwayèn laj anplwaye yo pou chak depatman.
mean_age_by_dept = df.groupby('department')['age'].mean()
print(mean_age_by_dept)

# graf pou Mwayèn laj anplwaye yo pou chak depatman.
plt.figure(figsize=(10, 6))
mean_age_by_dept.plot(kind='bar')
plt.title('Âge moyen des salariés par département')
plt.xlabel('Département')
plt.ylabel('Âge moyen')
plt.show()

# Mwayèn salè nan chak depatman
mean_salary_by_dept = df.groupby('department')['salary'].mean()
print(mean_salary_by_dept)

# graf pou Mwayèn salè nan chak depatman
plt.figure(figsize=(10, 6))
mean_salary_by_dept.plot(kind='bar')
plt.title('Salaire moyen dans chaque département')
plt.xlabel('Département')
plt.ylabel('Salaire moyen')
plt.show()

# Satisfaksyon travay sou chak depatman
mean_job_satisfaction_by_dept = df.groupby('department')['job_satisfaction'].mean()
print(mean_job_satisfaction_by_dept)

# graf pou Satisfaksyon travay sou chak depatman
plt.figure(figsize=(10, 6))
mean_job_satisfaction_by_dept.plot(kind='bar')
plt.title('Satisfaction au travail dans chaque département')
plt.xlabel('Département')
plt.ylabel('Satisfaction moyenne')
plt.show()

# Ki mwayèn tan ki genyen depi dènye fwa konpayi a te bay yon pwomosyon nan chak depatman?
mean_years_since_last_promotion_by_dept = df.groupby('department')['years_since_last_promotion'].mean()
print(mean_years_since_last_promotion_by_dept)

# graf pou mwayèn tan ki genyen depi dènye fwa konpayi a te bay yon pwomosyon nan chak depatman
plt.figure(figsize=(10, 6))
mean_years_since_last_promotion_by_dept.plot(kind='bar')
plt.title('Délai moyen depuis la dernière promotion par département')
plt.xlabel('Département')
plt.ylabel('Années depuis la dernière promotion')
plt.show()

# Bay mwayèn salè ki ekziste an fonksyon de nivo edikasyon anplwaye yo (Bachelor, Master)
mean_salary_by_education = df.groupby('education_level')['salary'].mean()
print(mean_salary_by_education)

# graf pou mwayèn salè ki ekziste an fonksyon de nivo edikasyon anplwaye yo (Bachelor, Master)
plt.figure(figsize=(10, 6))
mean_salary_by_education.plot(kind='bar')
plt.title('Salaire moyen en fonction du niveau d\'éducation')
plt.xlabel('Niveau d\'éducation')
plt.ylabel('Salaire moyen')
plt.show()














