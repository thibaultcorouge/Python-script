import pandas as pd

# Lecture des fichiers
df = pd.read_csv("data_source.csv", low_memory=False)
liste = pd.read_csv("filter_list.csv")

# Extraction des valeurs à conserver
value_to_keep = liste["column_name"].dropna().unique()

# Filtrage des données
df_filtre = df[df["column_name"].isin(value_to_keep)]

# Sauvegarde du résultat
df_filtre.to_csv("data_filtered.csv", index=False)

# Affichage des informations
print(f"Fichier filtre genere : {len(df_filtre)} lignes conservees sur {len(df)}")
print("Apercu des premieres lignes :")
print(df_filtre.head())
