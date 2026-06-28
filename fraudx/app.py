from flask import Flask, jsonify
from fraudx.db import SessionLocal
from fraudx.db import init_db
from fraudx.models import Transaction
from flask import request

from fraudx.fraud_model import predict_transaction


def create_app() -> Flask:

    app = Flask(__name__)

    init_db()

    @app.get("/health")
    def health():
        return jsonify({
            "status": "ok",
            "service": "FraudX AI"
        }), 200

    @app.get("/hello")
    def hello():
        return jsonify({
            "message": "Welcome to FraudX AI"
        }), 200
    

    
    @app.get("/db/stats")
    def stats():
        session = SessionLocal()

        total = session.query(Transaction).count()

        frauds = (
            session.query(Transaction)
            .filter(Transaction.fraud_label == 1)
            .count()
        )

        session.close()

        return jsonify({
            "transactions": total,
            "frauds": frauds
        })
    
    @app.get("/db/transactions")
    def transactions():
        session = SessionLocal()

        rows = (
            session.query(Transaction)
            .limit(20)
            .all()
        )

        data = []

        for r in rows:

            data.append({
                "id": r.id,
                "amount": r.amount,
                "fraud": r.fraud_label
            })

        session.close()

        return jsonify(data)
    

    @app.post("/fraud/predict")
    def fraud_predict():
        payload = request.get_json()

        if not payload:

            return jsonify({
                "error": "JSON manquant"
            }), 400

        features = payload.get("features")

        if not features:

            return jsonify({
                "error": "features manquant"
            }), 400

        try:

            result = predict_transaction(
                features
            )

            return jsonify(result)

        except Exception as e:

            return jsonify({
                "error": str(e)
            }), 500
        

    @app.get("/fraud/summary")
    def fraud_summary():
        session = SessionLocal()

        total = session.query(
            Transaction
        ).count()

        frauds = (
            session.query(Transaction)
            .filter(
                Transaction.fraud_label == 1
            )
            .count()
        )

        session.close()

        return jsonify({
            "total_transactions": total,
            "frauds": frauds,
            "fraud_rate": round(
                frauds / total * 100,
                3
            )
        })
    

    return app


if __name__ == "__main__":
    create_app().run(
        debug=True,
        port=5000
    )