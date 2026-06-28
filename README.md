# FraudX AI – Credit Card Fraud Detection

## Présentation

FraudX AI est une plateforme de détection de fraude bancaire développée dans le cadre du module d'Intelligence Artificielle.

Le projet adapte le pipeline FinSentiment (Finance) vers un système intelligent de détection de fraude sur cartes bancaires à partir du dataset Kaggle Credit Card Fraud Detection.

Le pipeline couvre l'ensemble du cycle :

* API Flask
* ETL et stockage SQLite
* Machine Learning (Random Forest)
* Dashboard Streamlit
* Tests automatisés
* CI/CD GitHub Actions

---

# Architecture globale

```text
Dataset Kaggle
      │
      ▼
 ETL Pipeline
      │
      ▼
 SQLite Database
      │
      ▼
 Machine Learning Model
(Random Forest)
      │
      ▼
 Flask REST API
      │
      ▼
 Streamlit Dashboard
      │
      ▼
 Hugging Face Spaces (optionel)
```

---

# Structure du projet

```text
fraudx-ai/
│
├── fraudx/
│   ├── __init__.py
│   ├── app.py
│   ├── db.py
│   ├── models.py
│   ├── fraud_model.py
│   │
│   └── etl/
│       ├── __init__.py
│       └── transactions_etl.py
│
├── dashboard/
│   └── app.py
│
├── scripts/
│   ├── run_etl.py
│   └── train_model.py
│
├── tests/
│   └── test_api.py
│
├── data/
│   ├── creditcard.csv
│   └── fraudx.db
│
├── models/
│   └── fraud_model.pkl
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── requirements.txt
├── README.md
└── app.py
```

---

# Dataset

Source :

Credit Card Fraud Detection Dataset (Kaggle)

Contenu :

* Time
* V1 à V28
* Amount
* Class

Classe :

* 0 = Transaction normale
* 1 = Transaction frauduleuse

Nombre total :

* 284 807 transactions
* 492 fraudes

---

# LAB 1 – API Flask

## Objectif

Créer une API REST minimale.

## Architecture

```text
Client
  │
  ▼
Flask API
```

## Endpoints

### GET /health

Vérification de disponibilité.

Réponse :

```json
{
  "status": "ok",
  "service": "FraudX AI"
}
```

### GET /hello

Réponse de test.

```json
{
  "message": "Welcome to FraudX AI"
}
```

## Étapes

1. Création du projet
2. Installation Flask
3. Création app.py
4. Tests manuels avec curl
5. Premier commit Git

---

# LAB 2 – ETL + SQLite

## Objectif

Importer les transactions dans une base SQLite.

## Architecture

```text
creditcard.csv
      │
      ▼
ETL Pipeline
      │
      ▼
SQLite Database
```

## Base de données

Table :

```sql
transactions
```

Champs :

```text
id
time
amount
v1 ... v28
fraud_label
```

## Étapes

### Étape 1

Installer :

```bash
pip install sqlalchemy pandas
```

### Étape 2

Créer :

```text
fraudx/db.py
fraudx/models.py
```

### Étape 3

Créer :

```text
fraudx/etl/transactions_etl.py
```

### Étape 4

Importer :

```bash
python scripts/run_etl.py
```

### Étape 5

Tester :

```bash
curl http://localhost:5000/db/stats
```

## Endpoints

### GET /db/stats

Retourne :

* nombre total de transactions
* nombre de fraudes

### GET /db/transactions

Retourne les 20 premières transactions.

---

# LAB 3 – Machine Learning

## Objectif

Créer un moteur de détection de fraude.

## Architecture

```text
Transactions
      │
      ▼
Random Forest
      │
      ▼
Prediction
```

## Modèle utilisé

RandomForestClassifier

Bibliothèque :

```python
sklearn.ensemble.RandomForestClassifier
```

## Étapes

### Étape 1

Installer :

```bash
pip install scikit-learn joblib
```

### Étape 2

Créer :

```text
scripts/train_model.py
```

### Étape 3

Entraîner :

```bash
python scripts/train_model.py
```

### Étape 4

Sauvegarder :

```text
models/fraud_model.pkl
```

### Étape 5

Créer :

```text
fraudx/fraud_model.py
```

### Étape 6

Créer endpoint :

```text
POST /fraud/predict
```

## Exemple

```json
{
  "prediction": "FRAUD",
  "fraud_probability": 0.93
}
```

## Endpoint résumé

### GET /fraud/summary

Retourne :

```json
{
  "total_transactions": 284807,
  "frauds": 492,
  "fraud_rate": 0.173
}
```

---

# LAB 4 – Dashboard Streamlit

## Objectif

Visualiser les données et les résultats du modèle.

## Architecture

```text
Flask API
      │
      ▼
Streamlit Dashboard
      │
      ▼
Utilisateur
```

## Fonctionnalités

### KPI

* Nombre de transactions
* Nombre de fraudes
* Taux de fraude

### Graphiques

* Histogramme des montants
* Répartition fraude / normal
* Transactions frauduleuses

### Simulation

Prédiction d'une transaction.

## Lancement

```bash
streamlit run dashboard/app.py
```

---

# LAB 5 – Tests et CI/CD

## Objectif

Automatiser les vérifications.

## Architecture

```text
GitHub
   │
   ▼
GitHub Actions
   │
   ▼
pytest + flake8
```

## Tests

### test_health

Vérifie :

```text
GET /health
```

### test_hello

Vérifie :

```text
GET /hello
```

## Workflow

Fichier :

```text
.github/workflows/ci.yml
```

## Vérifications

```bash
pytest
flake8
```

---

# Endpoints finaux

| Méthode | Endpoint         | Description       |
| ------- | ---------------- | ----------------- |
| GET     | /health          | Vérification API  |
| GET     | /hello           | Test API          |
| GET     | /db/stats        | Statistiques base |
| GET     | /db/transactions | Transactions      |
| POST    | /fraud/predict   | Détection fraude  |
| GET     | /fraud/summary   | Résumé fraude     |

---

# Technologies utilisées

* Python 3.11
* Flask
* SQLAlchemy
* SQLite
* Pandas
* Scikit-Learn
* Joblib
* Streamlit
* Plotly
* Pytest
* Flake8
* GitHub Actions

---

# Auteur

Projet réalisé dans le cadre du module IA.

FraudX AI – Credit Card Fraud Detection System.

RANIA HEDHLI ECOFIQ
Mariem Ben Rejeb
