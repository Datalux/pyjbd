def exists(list, name):
    for db in list:
        if db['name'] == name:
            return db
    return False

