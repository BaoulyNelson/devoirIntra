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

# annal chaje fichye a
file_path = 'company.csv'
df = pd.read_csv(file_path)

#konveti sale a an string majiskil
df['salary'] = df['salary'].str.upper()

#fonksyon pou retirer vigil ak let k nan sale a
def convert_salary(salary):
    if pd.isna(salary):
        return salary
    salary = salary.upper().replace(',', '') 
    if 'K' in salary:
        return float(salary.replace('K', '')) * 1000
    return float(salary)

#aplike fonksyon an la
df['salary'] = df['salary'].apply(convert_salary)
df['salary'] = df['salary'].astype('Float64')

#Siprime liy vid
df.dropna(inplace=True)

# konveti kolonn sale an float
df['salary'] = pd.to_numeric(df['salary'], errors='coerce')


# retire mot year la nn kolonn years_at_company
df['years_at_company'] = df['years_at_company'].str.replace(r'\D+', '', regex=True)

#ranplase ak mete an majiskil vale ki nan kolonn gender pa m ou f
df['gender'] = df['gender'].str.upper()
df['gender'] = df['gender'].replace({'MALE': 'M', 'FEMALE': 'F'})

#konveti dat lan en 4 foma diferan ak kolon tampore
df['hired_date_1'] = pd.to_datetime(df['hired_date'], format='%d-%b-%y', errors='coerce')
df['hired_date_2'] = pd.to_datetime(df['hired_date'], format='%d-%b-%Y', errors='coerce')
df['hired_date_3'] = pd.to_datetime(df['hired_date'], format='%d-%m-%Y', errors='coerce')
df['hired_date_4'] = pd.to_datetime(df['hired_date'], format='%d-%m-%y', errors='coerce')

#konbine rezilta 4 kovesyon yo
df['hired_date'] = df['hired_date_1'].combine_first(df['hired_date_2']).combine_first(df['hired_date_3']).combine_first(df['hired_date_4'])
#siprime kolon tanpore
df.drop(columns=['hired_date_1', 'hired_date_2', 'hired_date_3', 'hired_date_4'], inplace=True)
# fomate kolon lan an jou,mw ak ane
df['hired_date'] = df['hired_date'].dt.strftime('%d-%m-%Y')

# nou verifye ak konveti lot kolon si sa nesese
df['age'] = pd.to_numeric(df['age'], errors='coerce')
df['job_satisfaction'] = pd.to_numeric(df['job_satisfaction'], errors='coerce')
df['performance_score'] = pd.to_numeric(df['performance_score'], errors='coerce')
df['last_promotion_year'] = pd.to_numeric(df['last_promotion_year'], errors='coerce')

#Repatisyon chak anplwaye nan chak depatman.
repatisyon_depatman = df['department'].value_counts()
print(repatisyon_depatman)

# graf pou Repatisyon chak anplwaye nan chak depatman.
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='department')
plt.title('Repatisyon chak anplaye nn chak depatman')
plt.xlabel('Depatman')
plt.ylabel('Kantite anplwaye')
plt.show()

# Repatisyon pa sèks nan chak depatman.
repatisyon_seks_depatman = df.groupby(['department', 'gender']).size()
print(repatisyon_seks_depatman)

#graf pou Repatisyon pa sèks nan chak depatman.
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='department', hue='gender')
plt.title('Repatisyon par seks chak anplaye nn chak depatman')
plt.xlabel('Depatman')
plt.ylabel('Kantite anplwaye')
plt.show()

# Mwayèn laj anplwaye yo pou chak depatman.
laj_mwayen_anplaye = df.groupby('department')['age'].mean()
print(laj_mwayen_anplaye)

# graf pou Mwayèn laj anplwaye yo pou chak depatman.
plt.figure(figsize=(10, 6))
laj_mwayen_anplaye.plot(kind='bar')
plt.title('Laj mwayenn anplaye pou chak depatman')
plt.xlabel('Depatman')
plt.ylabel('laj mwayenn')
plt.show()

# salè Mwayèn nan chak depatman
sale_mwayenn = df.groupby('department')['salary'].mean()
print(sale_mwayenn)

# graf pou Mwayèn salè nan chak depatman
plt.figure(figsize=(10, 6))
sale_mwayenn.plot(kind='bar')
plt.title('Sale mwayenn nan chak deptaman')
plt.xlabel('Depatman')
plt.ylabel('Sale mwayenn ')
plt.show()

# Satisfaksyon travay sou chak depatman
satisfaksyon_travay = df.groupby('department')['job_satisfaction'].mean()
print(satisfaksyon_travay)

# graf pou Satisfaksyon travay sou chak depatman
plt.figure(figsize=(10, 6))
satisfaksyon_travay.plot(kind='bar')
plt.title('Satisfaskyon nan travay chak depatman')
plt.xlabel('Depatman')
plt.ylabel('Mwayenn satisfaksyon')
plt.show()


# Moyenne de Temps Depuis la Dernière Promotion par Département
ane_kouran = pd.to_datetime('today').year
df['ane_dpi_denye_pwomosyon'] = ane_kouran - df['last_promotion_year']
# Ki mwayèn tan ki genyen depi dènye fwa konpayi a te bay yon pwomosyon nan chak depatman?
mwayenn_tan_pwomosyon = df.groupby('department')['ane_dpi_denye_pwomosyon'].mean()
print(mwayenn_tan_pwomosyon)

# graf pou mwayèn tan ki genyen depi dènye fwa konpayi a te bay yon pwomosyon nan chak depatman
plt.figure(figsize=(10, 6))
mwayenn_tan_pwomosyon.plot(kind='bar')
plt.title('Mwayenn ane denye pwomosyon pa depatman')
plt.xlabel('Depatman')
plt.ylabel('Ane depi denye pwomosyon')
plt.show()

#mwayenn sale an fonksyon de nivo edikasyon anplwaye yo (Bachelor, Master)
mwayenn_sale = df.groupby('education_level')['salary'].mean()
print(mwayenn_sale)

# graf pou salè mwayèn ki ekziste an fonksyon de nivo edikasyon anplwaye yo (Bachelor, Master)
plt.figure(figsize=(10, 6))
mwayenn_sale.plot(kind='bar')
plt.title('Sale mwayenn pa nivo edikasyon')
plt.xlabel('Nivo Edikasyon')
plt.ylabel('Mwayenn_sale')
plt.show()

print(df)



