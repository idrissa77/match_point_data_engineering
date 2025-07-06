import sqlite3
import pandas as pd
import json
import os

def compute_monitoring(db_path="storage/products.db", missing_json_path="reports/missing_values_report.json", output_json="reports/monitoring.json"):
    # Connexion à la base de données SQLite
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT * FROM products", conn)
    conn.close()

    # Colonnes critiques pour juger si un produit est "valide"
    critical_cols = ["product_name", "nutriscore_grade", "nova_group"]

    # Calcul des KPIs principaux
    total_products = len(df)
    valid_products = df.dropna(subset=critical_cols)
    percent_valid_products = round(len(valid_products) / total_products * 100, 2)

    nutriscore_distribution = df["nutriscore_grade"].value_counts(dropna=False).to_dict()
    avg_health_score = round(df["health_score"].mean(), 2)

    # Chargement du rapport de valeurs manquantes existant
    with open(missing_json_path, "r", encoding="utf-8") as f:
        missing_report = json.load(f)

    # Dictionnaire final
    monitoring_report = {
        "total_products": total_products,
        "percent_valid_products": percent_valid_products,
        "nutriscore_distribution": nutriscore_distribution,
        "average_health_score": avg_health_score,
        "missing_values_report": missing_report
    }

    # Création du dossier de sortie s'il n'existe pas
    os.makedirs(os.path.dirname(output_json), exist_ok=True)

    # Sauvegarde du rapport JSON
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(monitoring_report, f, indent=4, ensure_ascii=False)

    print(f"[✓] Rapport de monitoring sauvegardé dans {output_json}")

if __name__ == "__main__":
    compute_monitoring()
