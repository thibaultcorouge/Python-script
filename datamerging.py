import pandas as pd
from datetime import date

# Configuration des sources de donnees
SOURCES = [
    {"file": "source1.csv", "category": "category1", "subcol": "subtype1"},
    {"file": "source2.csv", "category": "category2", "subcol": "subtype2"},
    {"file": "source3.csv", "category": "category3", "subcol": "subtype3"}
]

# Colonnes standardisees pour le fichier final
STANDARD_COLUMNS = [
    "name", "brand", "opening_hours", "category", "subcategory",
    "addr_city", "addr_housenumber", "addr_street", "addr_postcode",
    "latitude", "longitude"
]

def normalize(df, required_cols):
    """Ajoute les colonnes manquantes et reordonne"""
    for col in required_cols:
        if col not in df.columns:
            df[col] = None
    return df[required_cols]

# Lecture et preparation des sources
dataframes = []

for source in SOURCES:
    df = pd.read_csv(source["file"])
    df["category"] = source["category"]
    
    # Renommage des colonnes specifiques
    rename_dict = {
        source["subcol"]: "subcategory",
        "lat": "latitude",
        "lon": "longitude"
    }
    df = df.rename(columns=rename_dict)
    
    # Normalisation
    df = normalize(df, STANDARD_COLUMNS)
    dataframes.append(df)

# Fusion de tous les dataframes
merged = pd.concat(dataframes, ignore_index=True)

# Nettoyage et dedoublonnage
merged = merged.drop_duplicates(subset=["name", "latitude", "longitude"], keep="first")
merged = merged.dropna(subset=["latitude", "longitude"])

# Ajout de metadata
merged["last_update"] = str(date.today())

# Sauvegarde
OUTPUT_FILE = "merged_data.csv"
merged.to_csv(OUTPUT_FILE, index=False)
print(f"Fusion terminee : {len(merged)} lignes dans {OUTPUT_FILE}")
