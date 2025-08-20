from api.lands.lands import get_land_data_with_cursor
from api.utils.deep_rice_utils import readable_point

def get_node(_node_id, cursor):
    query = """
                SELECT 
                    title,
                    ST_AsText(global_location) AS location, -- Convertit le point en texte (WKT)
                    created_at,
                    id,
                    ref
                FROM potos
                WHERE id = %s
                """

    cursor.execute(query, (_node_id,))
    result = cursor.fetchone()

    if result:
        title, location_wkt, created_at, _id, ref = result
        latitude, longitude = readable_point(location_wkt)

        return {
            "id": _id,
            "title": title,
            "location": {"latitude": latitude, "longitude": longitude},
            "created_at": created_at,
            "ref": ref
        }

    return None

def get_nodes(_land_id, cursor):
    land = get_land_data_with_cursor(land_id=_land_id, cursor=cursor)
    nodes = get_all_nodes(cursor)
    param = {
        "potos" : nodes,
        "land" : land
    }
    return param


def get_all_nodes(cursor):
    query = """
            SELECT 
                title,
                ST_AsText(global_location) AS location, -- Convertit le point en texte (WKT)
                created_at,
                id,
                ref
            FROM potos
            """

    cursor.execute(query)
    results = cursor.fetchall()

    nodes_list = []
    for result in results:
        title, location_wkt, created_at, _id, ref = result
        latitude, longitude = readable_point(location_wkt)

        nodes_list.append({
            "id": _id,
            "title": title,
            "location": {"latitude": latitude, "longitude": longitude},
            "created_at": created_at,
            "ref": ref
        })

    return nodes_list
