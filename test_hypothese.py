#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
from scipy import stats

# Chargement des données exportées depuis un fichier CSV
data = pd.read_csv(r"C:\Users\wassi\Desktop\Mes CV et mes resumes - V2\Alternance\Companies\ekwateur\data\conversion_rate_data.csv")

# Nettoyage des colonnes en supprimant les symboles de pourcentage, les virgules, et les espaces
# Les taux de conversion sont ensuite convertis en valeurs décimales (par exemple, 50% devient 0.5)
data['Conversion_rate_A'] = data['Conversion_rate_A'].str.replace(',', '.').str.replace('%', '').str.strip().astype(float) / 100
data['Conversion_rate_B'] = data['Conversion_rate_B'].str.replace(',', '.').str.replace('%', '').str.strip().astype(float) / 100

# Filtre des données en supprimant les valeurs manquantes (NaN) pour chaque version
conversion_A = data['Conversion_rate_A'].dropna()
conversion_B = data['Conversion_rate_B'].dropna()

# Affichage des taux de conversion nettoyés pour les versions A et B
print("Taux de conversion A après nettoyage :\n", conversion_A)
print("Taux de conversion B après nettoyage :\n", conversion_B)

# Début du test d'hypothèse statistique
# Réalisation d'un test t pour comparer les moyennes des taux de conversion entre les versions A et B
# Le test est effectué seulement s'il y a plus d'une observation pour chaque version
if len(conversion_A) > 1 and len(conversion_B) > 1:
    t_stat, p_value = stats.ttest_ind(conversion_A, conversion_B)
else:
    t_stat, p_value = None, None

# Calcul des statistiques descriptives pour les deux versions
desc_A = conversion_A.describe()
desc_B = conversion_B.describe()

# Calcul de la variance pour les deux versions
variance_A = conversion_A.var()
variance_B = conversion_B.var()

# Préparation des résultats sous forme de dictionnaire pour l'exportation
results = {
    "Mean_A": [desc_A['mean']],
    "StdDev_A": [desc_A['std']],
    "Variance_A": [variance_A],
    "Mean_B": [desc_B['mean']],
    "StdDev_B": [desc_B['std']],
    "Variance_B": [variance_B],
    "T-statistic": [t_stat],
    "P-value": [p_value]
}

# Création d'un DataFrame à partir des résultats pour faciliter l'exportation
results_df = pd.DataFrame(results)

# Sauvegarde des résultats du test t et des statistiques descriptives dans un fichier CSV
results_df.to_csv(r"C:\Users\wassi\Desktop\Mes CV et mes resumes - V2\Alternance\Companies\ekwateur\data\t_test_results.csv", index=False)

# Message indiquant que les résultats ont été sauvegardés
print("Results have been saved to 't_test_results.csv'")


# In[ ]:




