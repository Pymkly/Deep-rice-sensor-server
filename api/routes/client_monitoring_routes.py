from fastapi import APIRouter

from api.database.connection import get_connection
from api.monitoring.sensor_node import get_nodes

router = APIRouter()

conn = get_connection()

@router.get("/monitoring/{land_id}")
async def refresh_rag(land_id: int):
    cursor = conn.cursor()
    result = get_nodes(land_id, cursor)
    cursor.close()
    return result
