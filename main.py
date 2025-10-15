from ops_instrumentation import attach_ops
from fastapi import FastAPI
from datetime import datetime
from utils.inference import get_price_recommendation

app = FastAPI()
attach_ops(app)

@app.get("/rl-pricing")
async def rl_pricing():
    try:
        result = get_price_recommendation()
        return {
            "model": "rl-pricing-v1.0.0",
            "status": "online",
            "lastUpdated": str(datetime.utcnow().date()),
            "data": result
        }
    except Exception as e:
        return {
            "model": "rl-pricing-v1.0.0",
            "status": "offline",
            "lastUpdated": str(datetime.utcnow().date()),
            "data": {"error": "API call failed", "details": str(e)}
        }
