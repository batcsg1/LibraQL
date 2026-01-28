from engine import LibraDB

# Initialize the database
db = LibraDB("my_database.toon")

# Initialize a collection
users = db.collection("users")

# Find all users
allUsers = users.find()

# Find specific users

# Sort users
# allUsers = users.find(sort={"age": 1})
# Retrieve a specific number of users

# Show a specific amount of fields of the user object

# Insert a user
# newUser = users.insert({ "name": "Brent", "age": 21 })

print(allUsers)
