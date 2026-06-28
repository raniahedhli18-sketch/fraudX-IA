import pandas as pd

from fraudx.db import SessionLocal
from fraudx.models import Transaction


def ingest_transactions(csv_path):

    df = pd.read_csv(csv_path)

    session = SessionLocal()

    for _, row in df.iterrows():
        tx = Transaction(
            time=row["Time"],
            amount=row["Amount"],
            v1=row["V1"],
            v2=row["V2"],
            v3=row["V3"],
            v4=row["V4"],
            v5=row["V5"],
            v6=row["V6"],
            v7=row["V7"],
            v8=row["V8"],
            v9=row["V9"],
            v10=row["V10"],
            v11=row["V11"],
            v12=row["V12"],
            v13=row["V13"],
            v14=row["V14"],
            v15=row["V15"],
            v16=row["V16"],
            v17=row["V17"],
            v18=row["V18"],
            v19=row["V19"],
            v20=row["V20"],
            v21=row["V21"],
            v22=row["V22"],
            v23=row["V23"],
            v24=row["V24"],
            v25=row["V25"],
            v26=row["V26"],
            v27=row["V27"],
            v28=row["V28"],
            fraud_label=row["Class"],
        )

        session.add(tx)

    session.commit()

    session.close()

    print(f"{len(df)} transactions importées")
