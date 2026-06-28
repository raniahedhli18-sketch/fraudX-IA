from fraudx.db import init_db
from fraudx.etl.transactions_etl import ingest_transactions

init_db()

ingest_transactions("data/creditcard.csv")
