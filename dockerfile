# Base image officielle Python
FROM python:3.10-slim

# Dossier de travail dans le container
WORKDIR /app

# Copier les fichiers requirements.txt (à créer) et le code
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Commande par défaut pour exécuter le pipeline
CMD ["python", "run_pipeline.py"]
