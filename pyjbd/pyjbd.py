import json
import os
import shutil

from pyjbd import dbutils as utils
from pyjbd.exceptions import *


class pyjbd:
    db_list = []
    db_prefs = None

    def __init__(self):
        self.local_path = os.getcwd()

    def create_database(self, name):
        db = {
            'name': name,
            'path': self.local_path + '/' + name,
            'ref': name + '.json'
        }

        os.mkdir(db['path'])
        os.chdir(db['path'])
        with open(db['ref'], 'w') as db_name:
            tmp_db = {}
            json.dump(tmp_db, db_name)

        self.db_list.append(db)

    def delete_database(self, db_name):
        db = utils.exists(self.db_list, db_name)
        if db:
            shutil.rmtree(db['path'])
        else:
            raise DatabaseError

    def set_db(self, db_name):
        db = utils.exists(self.db_list, db_name)
        if db:
            self.db_prefs = db
            os.chdir(db['path'])
        else:
            raise DatabaseError


    def dump(self, db_name):
        db = utils.exists(self.db_list, db_name)
        if db:
            with open(db['ref']) as _db:
                data = json.loads(_db.read())
                return data
        else:
            raise DatabaseError

    def add(self, key, value):
        with open(self.db_prefs['ref'], "r") as jf:
            data = json.loads(jf.read())

        data[key] = value

        with open(self.db_prefs['ref'], "w") as jf:
            json.dump(data, jf)

    def delete(self, key):
        with open(self.db_prefs['ref'], "r") as jf:
            data = json.loads(jf.read())

        if key in data:
            data.pop(key, None)
        else:
            raise KeyNotFound

        with open(self.db_prefs['ref'], "w") as jf:
            json.dump(data, jf)

    def update(self, key, new_value):
        with open(self.db_prefs['ref'], "r") as jf:
            data = json.loads(jf.read())

        if key in data:
            data[key] = new_value
        else:
            raise KeyNotFound

        with open(self.db_prefs['ref'], "w") as jf:
            json.dump(data, jf)

    def get(self, key):
        with open(self.db_prefs['ref'], "r") as jf:
            data = json.loads(jf.read())

            if key in data:
                return data[key]
            else:
                raise KeyNotFound
