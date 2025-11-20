# Scripts de traitement de données

Collection de scripts Python pour nettoyer et fusionner des données structurées.

## Description

Ce dépôt contient des outils pour traiter des fichiers de données et produire des datasets CSV organisés. Les scripts sont conçus pour être génériques et réutilisables sur différents types de données.

## Prérequis

- Python 3.7 ou supérieur
- pandas

Installation des dépendances :
```bash
pip install pandas
```

## Scripts disponibles

### scriptcleaning.py

Filtre un dataset selon une liste de valeurs autorisées.

Utilisation :
- Place les fichiers source et la liste de filtrage dans le même répertoire
- Ajuste les noms de fichiers et colonnes selon tes besoins
- Lance le script pour obtenir un fichier filtré

Fonctionnement :
- Lit un fichier de données principal
- Applique un filtre basé sur une liste de valeurs valides
- Exporte les lignes conservées dans un nouveau fichier

### datamerging.py

Fusionne plusieurs sources de données en un seul dataset unifié.

Fonctionnalités :
- Normalisation des colonnes entre sources
- Dédoublonnage basé sur critères configurables
- Ajout automatique de métadonnées
- Export consolidé au format CSV

Configuration :
- Modifie la liste `SOURCES` pour ajouter ou retirer des fichiers source
- Adapte `STANDARD_COLUMNS` selon tes besoins
- Personnalise les colonnes utilisées pour le dédoublonnage

## Utilisation générale

1. Prépare tes fichiers CSV sources
2. Configure les noms de fichiers et colonnes dans les scripts
3. Lance le script de nettoyage pour filtrer les données
4. Fusionne plusieurs sources si nécessaire
5. Récupère ton CSV final

## Structure des fichiers

Les scripts attendent des fichiers CSV avec encodage UTF-8. Les colonnes peuvent varier selon tes besoins, les scripts ajoutent automatiquement les colonnes manquantes avec des valeurs nulles.

## Notes

- Les fichiers volumineux sont traités efficacement grâce à pandas
- Le dédoublonnage supprime les lignes avec valeurs manquantes dans les colonnes critiques
- Une date de dernière mise à jour est ajoutée automatiquement lors de la fusion

## Licence

Ce projet est libre d'utilisation et de modification selon tes besoins.
