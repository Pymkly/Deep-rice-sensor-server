from fastapi import APIRouter

from api.database.connection import get_connection
from api.lands.lands import get_land_data_with_cursor

router = APIRouter()

conn = get_connection()

@router.get("/land/{land_id}")
def get_land_endpoint(land_id: int):
    cursor = conn.cursor()
    result = get_land_data_with_cursor(land_id, cursor)
    cursor.close()
    return result

