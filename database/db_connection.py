from utils.logger import log

fake_db = {
    "users": [],
    "orders": []
}

def insert(table, data):
    fake_db[table].append(data)
    log(f"Inserted into {table}: {data}")
    return data


def get_all(table):
    return fake_db.get(table, [])