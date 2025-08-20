from fastapi import WebSocket, WebSocketDisconnect, APIRouter

from api.monitoring.monitoring_manager import collect_last

# import asyncio
# from api.database.conn import get_mongo_db

router = APIRouter()

active_connections = {}

fake_sensor_data = [
    {
        "DHT22": {"Humidity": "30%", "Temperature": "6°C"},
        "NPK": {"N": "100", "P": "45", "K": "55"}
    },
    {
        "DHT22": {"Humidity": "40%", "Temperature": "10°C"},
        "NPK": {"N": "50", "P": "30", "K": "22"}
    }
]
t = 0
import json
@router.websocket("/monitoring")
async def web_socket(_websocket: WebSocket, id: int):
    print("eto")
    await _websocket.accept()
    try :
        active_connections[id].append(_websocket)
    except KeyError as e:
        active_connections[id] = [_websocket]
        print(e)
    data = collect_last(id)
    await _websocket.send_text(json.dumps(data))
    try:
        while True:
            # Garde la connexion active
            await _websocket.receive_text()
    except WebSocketDisconnect:
        active_connections[id].remove(_websocket)
        print("Client déconnecté.")



async def update_client_data():
    global t
    print("updated")
    for _node_id in active_connections.keys():
        data = collect_last(_node_id)
        print(data)
        for _websocket in active_connections[_node_id]:
            await _websocket.send_text(json.dumps(data))
        # t = 1 if t == 0 else 0

