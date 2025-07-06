# Projet Match Point Data Engineering — Pipeline Open Food Facts

## Contexte du projet
Ce projet a été réalisé dans le cadre d’une simulation professionnelle visant à reproduire un environnement de travail réel autour du développement de BuySmart, une application mobile imaginée par l’entreprise Match Point.

Pour ce faire, j’ai travaillé sur un pipeline Data Engineering complet en utilisant les données ouvertes du site Open Food Facts afin de traiter, analyser et valoriser des informations produit similaires à celles que BuySmart pourrait exploiter pour aider le consommateur à faire des choix éclairés en magasin.

---

## Objectifs du pipeline

- **Automatiser la collecte** des données produit depuis des sources fiables comme Open Food Facts.
- **Nettoyer et transformer** ces données afin d’avoir un format exploitable.
- **Stocker** ces données transformées dans un format et un emplacement optimisés pour la consultation par l’application mobile.
- **Contrôler la qualité** des données en vérifiant la présence de valeurs manquantes ou incohérentes.
- **Monitorer** le pipeline pour détecter rapidement toute anomalie ou échec d’exécution.

---

## Description détaillée du projet

### 1. Ingestion des données

- Extraction automatisée des données produits depuis Open Food Facts (simulée ici).
- Chargement initial dans un format brut, avec horodatage pour assurer la traçabilité.

### 2. Transformation

- Nettoyage des données : suppression des doublons, correction des formats (dates, nombres).
- Enrichissement des données : calculs d’indicateurs santé/environnementaux à partir des informations brutes.
- Conversion dans un format standardisé compatible avec les besoins de l’application BuySmart.

### 3. Stockage

- Enregistrement des données transformées dans des fichiers CSV/Parquet ou une base de données.
- Organisation en dossiers/date pour faciliter l’accès et la gestion des versions.

### 4. Contrôle qualité

- Analyse des données pour détecter les valeurs manquantes ou aberrantes.
- Génération de rapports automatiques en cas d’erreurs ou de données suspectes.

### 5. Monitoring

- Suivi des performances du pipeline (temps d’exécution, ressources consommées).
- Notifications en cas d’échec ou de dépassement de seuils définis.

---

## Architecture technique

- **Python** est utilisé pour le scripting de chaque étape (ingestion, transformation, stockage, contrôle, monitoring).
- **Apache Airflow** orchestre l’ensemble via un DAG unique nommé `match_point_pipeline` : planification, exécution et suivi.
- Environnement virtuel Python (`venv`) avec dépendances gérées via `pip`.
- Les données et scripts sont organisés dans un dossier structuré (`dags/`, `scripts/`, `data/`).
- Versionnage du projet avec **Git** pour assurer traçabilité et collaboration.
- Documentation et logs accessibles pour garantir la maintenabilité.

---

## Déroulement du pipeline

Le DAG Airflow déclenche une tâche unique `run_pipeline` qui exécute successivement :

```python
def run_pipeline():
    ingestion.main()
    transformation.main()
    load.main()
    missing_values_checking.monitor_data_missing_values()
    monitoring.compute_monitoring()
