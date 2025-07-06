import requests
import pandas as pd
import time

# Fonction pour récupérer une liste de produits depuis Open Food Facts
def get_products_from_api(category="snacks", page_size=100, max_pages=3):
    base_url = "https://world.openfoodfacts.org/cgi/search.pl"
    products = []

    for page in range(1, max_pages + 1):
        params = {
            "action": "process",
            "tagtype_0": "categories",
            "tag_contains_0": "contains",
            "tag_0": category,
            "page_size": page_size,
            "page": page,
            "json": 1,
        }

        response = requests.get(base_url, params=params)
        if response.status_code != 200:
            print(f"Erreur page {page} : {response.status_code}")
            break

        data = response.json()
        page_products = data.get("products", [])

        for prod in page_products:
            products.append({
                "product_name": prod.get("product_name", ""),
                "brands": prod.get("brands", ""),
                "code": prod.get("code", ""),
                "categories": prod.get("categories", ""),
                "nutriscore_grade": prod.get("nutriscore_grade", ""),
                "nova_group": prod.get("nova_group", ""),
                "ecoscore_grade": prod.get("ecoscore_grade", ""),
                "url": prod.get("url", "")
            })

        print(f"[✓] Page {page} récupérée ({len(page_products)} produits)")
        time.sleep(1)  # pause pour ne pas surcharger l’API

    return pd.DataFrame(products)

# Fonction principale pour exécution depuis run_pipeline.py
def main():
    df = get_products_from_api(category="biscuits", page_size=100, max_pages=5)
    print(f"Total produits récupérés : {len(df)}")
    df.to_csv("produits_biscuits.csv", index=False)
    print("[✓] Données sauvegardées dans produits_biscuits.csv")

if __name__ == "__main__":
    main()
