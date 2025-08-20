import logging

import uvicorn
from api.routes.client_monitoring_routes import router as client_monitoring_router
from api.routes.land_routes import router as land_router
from api.routes.monitoring_routes import router as ws_router
from api.routes.raspberry_pi_routes import router as rasp_router
from fastapi import FastAPI
from pydantic import BaseModel

logging.basicConfig(
    filename='deep-rice.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
app = FastAPI()

app.include_router(land_router, prefix="/api")
app.include_router(rasp_router, prefix="/rasp")
app.include_router(ws_router, prefix="/ws")
app.include_router(client_monitoring_router, prefix="/api")

class QueryModel(BaseModel):
    query: str
@app.get("/ping")
async def ping():
    return {"message": "pong"}


if __name__ == '__main__':
    uvicorn.run("app:app", host="0.0.0.0",
                port=8000, reload=True)