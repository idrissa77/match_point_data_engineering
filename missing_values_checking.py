import pandas as pd
import json
import os

def monitor_data_missing_values(input_csv="produits_biscuits_clean.csv", output_json="reports/missing_values_report.json"):
    df = pd.read_csv(input_csv)

    missing_report = {}

    # Pour chaque colonne, on liste les index des lignes où la valeur est manquante
    for col in df.columns:
        missing_indexes = df[df[col].isnull()].index.tolist()
        missing_report[col] = {
            "missing_count": len(missing_indexes),
            "missing_rows": missing_indexes
        }

    # Créer le dossier "reports" s’il n'existe pas
    os.makedirs(os.path.dirname(output_json), exist_ok=True)

    # Sauvegarde du rapport complet dans le dossier reports
    with open(output_json, "w") as f:
        json.dump(missing_report, f, indent=4)

    print(f"[✓] Rapport des valeurs manquantes sauvegardé dans {output_json}")

if __name__ == "__main__":
    monitor_data_missing_values()
