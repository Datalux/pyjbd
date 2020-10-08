# pyjbd
A very small Python JSON Based Database

With **pyjbd** you can easly manage and use a database using JSON file!

### Some example
```Python
# create a new database or table
db.create_database("my-awesome-database")

# set the database to use 
db.set_db("my-awesome-database")

# add two diffent item
db.add("item1", "value1")
db.add("item2", "value2")

# print the database
print(db.dump("my-awesome-database"))
# will output:
# {"item1": "value1", "item2": "value2"}

# print the value of a key
print(db.get("item2"))
# will output:
# value1

# update the value of a key
db.update("item2", "new-item-2")

# delete a database
db.delete_database("my-awesome-database")
```
