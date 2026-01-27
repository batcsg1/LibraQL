from engine import LibraQL

# Initialize the database
db = LibraQL("my_database.toon")

# Initialize a collection
users = db.collection("users")

# Find all users
allUsers = users.find()

# Insert a user
# newUser = users.insert({ "name": "Brent", "age": 21 })

print(allUsers)