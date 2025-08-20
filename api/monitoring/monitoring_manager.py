from api.database.connection import get_connection, get_mongo_db_connection
from api.monitoring.sensor_node import get_node
from api.utils.deep_rice_utils import get_sensor_collections

con = get_connection()
client, db = get_mongo_db_connection()


def collect_details(ref):
    result = {}
    for collection_name in get_sensor_collections():
        collection = db[collection_name]

        latest_data = collection.find_one(
            {"ref": ref},
            sort=[("timestamp", -1)]
        )

        if latest_data and "data" in latest_data:
            raw_data  = latest_data["data"]
            formatted_data = {}
            for key, value in raw_data.items():
                if isinstance(value, (int, float)):
                    num = float(value)
                    num = round(num, 2)
                    print(num)
                    formatted_data[key] = f"{num:.2f}"
                else:
                    formatted_data[key] = value
            result[collection_name] = formatted_data
    return result


def collect_last(_node_id):
    cursor = con.cursor()
    _node = get_node(_node_id, cursor)
    _ref = _node["ref"]
    cursor.close()
    return collect_details(_ref)



