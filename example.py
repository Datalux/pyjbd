from pyjbd import pyjbd

db = pyjbd.pyjbd()

db.create_database("m")
db.set_db('m')
db.add("nome", "giuseppe")
db.add("cognome", "criscione")
db.add('list', [])
print(db.dump('m'))
db.update('list', [1, 2])
print(db.dump('m'))
print(db.get("cognome"))
db.delete("cognome")
print(db.dump("m"))
db.delete_database("m")

