import sqlite3 
import pandas as pd
import os

def main(
    input_csv="produits_biscuits_clean.csv",  # fichier nettoyé
    db_path="storage/products.db"             # base de données dans le dossier storage
):
    # Vérifie que le fichier CSV existe
    if not os.path.isfile(input_csv):
        raise FileNotFoundError(f"Le fichier CSV n'a pas été trouvé : {input_csv}")

    # Lecture des données
    df = pd.read_csv(input_csv)

    # Connexion à SQLite
    conn = sqlite3.connect(db_path)

    # Création de la table si elle n'existe pas
    conn.execute("""
        CREATE TABLE IF NOT EXISTS products (
            code TEXT PRIMARY KEY,
            product_name TEXT,
            brands TEXT,
            nutriscore_grade TEXT,
            health_score INTEGER,
            nova_group INTEGER,
            ecoscore_grade TEXT,
            quantity TEXT,
            labels TEXT,
            ingredients_text TEXT,
            additives_tags TEXT,
            allergens_tags TEXT,
            packaging TEXT,
            countries_tags TEXT,
            url TEXT,
            retrieval_date TEXT,
            price_eur REAL
        )
    """)

    # Insertion/remplacement des données
    df.to_sql("products", conn, if_exists="replace", index=False)

    conn.commit()
    conn.close()

    print(f"[✓] Données chargées dans la base SQLite : {os.path.abspath(db_path)}")

if __name__ == "__main__":
    main()
