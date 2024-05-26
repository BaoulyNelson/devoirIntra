"""
Pwojè an gwoup (7 moun maksimòm)
Objektif prensipal pwojè sa, se kreye yon koleksyon done ki byen prepare pou vizyalizasyon. Wap gen pou w itilize, netwaye, transfòme done sa yo ak libreri Python pandas ak numpy.

Sa vle di wap jere valè ki manke yo (NaN), detekte kolòn ki merite transfòme an lòt tip done, epi aplike analiz estatistik bazik oubyen avanse.

Kesyon sou Analiz Demografik
Repatisyon chak anplwaye nan chak depatman.
Repatisyon pa sèks nan chak depatman.
Mwayèn laj anplwaye yo pou chak depatman.
Kesyon sou Salè
Mwayèn salè nan chak depatman
Satisfaksyon travay sou chak depatman
Kesyon sou Pwomosyon ak Edikasyon
Ki mwayèn tan ki genyen depi dènye fwa konpayi a te bay yon pwomosyon nan chak depatman?
Bay mwayèn salè ki ekziste an fonksyon de nivo edikasyon anplwaye yo (Bachelor, Master)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



# Charger le fichier CSV
df = pd.read_csv('C:/Users/elcon/Documents/ESIH 4EME ANNEE LICENSE/SESSIONII/PythonDataOriented/CSV FILES/company.csv')


# Afficher un aperçu des données
print(df.head())
print(df.info())

# Vérifier les valeurs manquantes
print(df.isnull().sum())

# Remplir les valeurs manquantes pour 'gender' par le mode (valeur la plus fréquente)
df['gender'].fillna(df['gender'].mode()[0], inplace=True)

# Suppression des lignes avec trop de valeurs manquantes si nécessaire
# df.dropna(thresh=len(df.columns)-2, inplace=True)

# Convertir 'hired_date' en type datetime
df['hired_date'] = pd.to_datetime(df['hired_date'], errors='coerce')

# Convertir 'salary' en format numérique en supprimant les caractères non numériques
df['salary'] = df['salary'].replace('[\$,K]', '', regex=True).astype(float)

# Convertir 'years_at_company' en format numérique en supprimant les caractères non numériques
df['years_at_company'] = df['years_at_company'].replace('[^0-9]', '', regex=True).astype(float)

# Vérifier et convertir d'autres colonnes si nécessaire
df['age'] = pd.to_numeric(df['age'], errors='coerce')
df['job_satisfaction'] = pd.to_numeric(df['job_satisfaction'], errors='coerce')
df['performance_score'] = pd.to_numeric(df['performance_score'], errors='coerce')
df['last_promotion_year'] = pd.to_numeric(df['last_promotion_year'], errors='coerce')

# Re-vérifier les informations générales après les conversions
print(df.info())

# Ajouter une colonne 'years_since_last_promotion'
current_year = pd.Timestamp.now().year
df['years_since_last_promotion'] = current_year - df['last_promotion_year']

# Répartition de chaque employé dans chaque département
dept_distribution = df['department'].value_counts()
print(dept_distribution)

# Répartition par sexe dans chaque département
gender_dept_distribution = df.groupby(['department', 'gender']).size().unstack()
print(gender_dept_distribution)

# Âge moyen des salariés par département
mean_age_by_dept = df.groupby('department')['age'].mean()
print(mean_age_by_dept)

# Salaire moyen dans chaque département
mean_salary_by_dept = df.groupby('department')['salary'].mean()
print(mean_salary_by_dept)

# Satisfaction au travail dans chaque département
mean_job_satisfaction_by_dept = df.groupby('department')['job_satisfaction'].mean()
print(mean_job_satisfaction_by_dept)

# Délai moyen depuis la dernière promotion par département
mean_years_since_last_promotion_by_dept = df.groupby('department')['years_since_last_promotion'].mean()
print(mean_years_since_last_promotion_by_dept)

# Salaire moyen en fonction du niveau d'éducation
mean_salary_by_education = df.groupby('education_level')['salary'].mean()
print(mean_salary_by_education)

# Répartition de chaque employé dans chaque département
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='department')
plt.title('Répartition de chaque employé dans chaque département')
plt.xlabel('Département')
plt.ylabel('Nombre d\'employés')
plt.show()

# Répartition par sexe dans chaque département
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='department', hue='gender')
plt.title('Répartition par sexe dans chaque département')
plt.xlabel('Département')
plt.ylabel('Nombre d\'employés')
plt.show()

# Âge moyen des salariés par département
plt.figure(figsize=(10, 6))
mean_age_by_dept.plot(kind='bar')
plt.title('Âge moyen des salariés par département')
plt.xlabel('Département')
plt.ylabel('Âge moyen')
plt.show()

# Salaire moyen dans chaque département
plt.figure(figsize=(10, 6))
mean_salary_by_dept.plot(kind='bar')
plt.title('Salaire moyen dans chaque département')
plt.xlabel('Département')
plt.ylabel('Salaire moyen')
plt.show()

# Satisfaction au travail dans chaque département
plt.figure(figsize=(10, 6))
mean_job_satisfaction_by_dept.plot(kind='bar')
plt.title('Satisfaction au travail dans chaque département')
plt.xlabel('Département')
plt.ylabel('Satisfaction moyenne')
plt.show()

# Délai moyen depuis la dernière promotion par département
plt.figure(figsize=(10, 6))
mean_years_since_last_promotion_by_dept.plot(kind='bar')
plt.title('Délai moyen depuis la dernière promotion par département')
plt.xlabel('Département')
plt.ylabel('Années depuis la dernière promotion')
plt.show()

# Salaire moyen en fonction du niveau d'éducation
plt.figure(figsize=(10, 6))
mean_salary_by_education.plot(kind='bar')
plt.title('Salaire moyen en fonction du niveau d\'éducation')
plt.xlabel('Niveau d\'éducation')
plt.ylabel('Salaire moyen')
plt.show()
