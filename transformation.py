import pandas as pd

# Dictionnaire de conversion nutriscore → score santé numérique
NUTRISCORE_MAP = {"a": 5, "b": 4, "c": 3, "d": 2, "e": 1}

def main(input_csv="produits_biscuits.csv", output_csv="produits_biscuits_clean.csv"):
    # Charger les données brutes
    df = pd.read_csv(input_csv)

    # Supprimer les doublons basés sur le code-barres
    df = df.drop_duplicates(subset=["code"])

    # Supprimer les lignes sans nom de produit
    df = df[df["product_name"].notna() & (df["product_name"].str.strip() != "")]

    # Nettoyer les valeurs du nutriscore (mettre en minuscules, supprimer les invalides)
    df["nutriscore_grade"] = df["nutriscore_grade"].str.lower().str.strip()
    df = df[df["nutriscore_grade"].isin(NUTRISCORE_MAP.keys())]

    # Ajouter une colonne score santé numérique (A=5, E=1)
    df["health_score"] = df["nutriscore_grade"].map(NUTRISCORE_MAP)

    # Nettoyer les noms de produit (minuscules, sans espaces inutiles)
    df["product_name"] = df["product_name"].str.lower().str.strip()

    # Sauvegarder les données nettoyées dans un nouveau fichier CSV
    df.to_csv(output_csv, index=False)
    print(f"[✓] Données nettoyées sauvegardées dans {output_csv}")

if __name__ == "__main__":
    main()
