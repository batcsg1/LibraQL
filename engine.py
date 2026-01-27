import os
from toon import encode, decode
from logger import Colors, Logger

logger = Logger(".\logs\log")
colors = Colors()

# the main database engine which reads and writes to a TOON file (Data persistence layer)
class LibraQL:
    # Name and load the database file
    def __init__(self, db_name="db.toon"):
        logger._log(colors.success, f"Intializing database with filename: {db_name}")
        self.db_name = db_name
        self.data = self._load()
    
    # Load the database into a TOON file or create the TOON file
    def _load(self):
        # If the file doesn't exist, create an empty file
        if not os.path.exists(self.db_name):
            print(f"Database file {self.db_name} not found. Creating a new one.")
            with open(self.db_name, 'w') as f:
                f.write("")
            return {}
        
        #Open and read the database file
        with open(self.db_name, 'r') as f:
            try:
                # Read from the file
                encoded_data = f.read()

                # Convert TOON data into dictionary
                decoded_data = decode(encoded_data)

                # If there is TOON data return the TOON data, otherwise return an empty dictionary
                return decoded_data if decoded_data else {}
            except Exception as e:
                # If there is a problem reading the TOON file, e.g. if the file is empty.
                print(f"Error reading database file: {e}")
                return {}
              
    # Saves the current state of the database to the database file
    def _save(self):
        # Open and write to the database file
        with open(self.db_name, 'w') as f:
            try:
                # write the data dictionary into TOON data
                encoded_data = encode(self.data)
                f.write(encoded_data)
            except Exception as e:
                # If there is a problem reading the TOON file, e.g. if the file is empty.
                print(f"Error writing to database file: {e}")
            
    # Creating a data collection
    def collection(self, name):
        # If there is no data collection
        if name not in self.data:
            # Add a list for the new collection to the 'master' data dictionary (self.data)
            self.data[name] = []
        # Return the new data collection
        return Collection(self, name)
    
# Collection class to handle operations on a specific collection (Data access layer)
class Collection:
    # Reference the engine, and initialize a new data collection
    def __init__(self, engine, name):
        self.engine = engine
        self.name = name
        print(f"Collection '{self.name}' initialized.")

    # Insert into the collection
    def insert(self, data):
        print(f"Inserting data into collection '{self.name}': {data}")

        # Add to the collection list
        self.engine.data[self.name].append(data)

        # Write the list to the database file
        self.engine._save()

    # Select from the collection
    def find(self, query=None):
        print(f"Finding data in collection '{self.name}'")

        # Get the data from the collection list, return an empty list if there is no data, hence the '[]'
        data = self.engine.data.get(self.name, [])

        # If no query is provided, return all records
        if not query:
            print("No query provided, returning all records.")
            #return encode(data)
            return data
                
        # Find items that match what is specified in the query
        def matches(item):
            # Check each key-value pair in the query
            for k, v in query.items():

                #{"age": {"$gt": 25}} Query example
                
                #query.items() = dict_items([( k: 'age', v: {'$gt': 25})])

                # Get the current value of the item from the collection

                val = item.get(k) #E.g. val = {"age": 25}, val would be 25

                # if the value (v) of the query is a dictionary
                if isinstance(v, dict):
                    # Logical check for operators
                    if "$gt" in v and not (val > v["$gt"]): return False
                    if "$lt" in v and not (val < v["$lt"]): return False
                    if "$gte" in v and not (val >= v["$gte"]): return False
                    if "$lte" in v and not (val <= v["$lte"]): return False
                elif val != v:
                    return False
            return True

        # Filter the data collection for values that match what was asked for in the query and return the results as a list
        return list(filter(matches, data))

    # Update the collection
    def update(self, query, new_data):
        print(f"Updating data in collection '{self.name}' with query: {query} and new data: {new_data}")

        # Find matching documents
        data = self.find(query)

        # If no documents match the query
        if not data:
            print("No documents matched the query. Nothing updated.")
            return 0

        # Update the matching documents
        for item in data:
            item.update(new_data)

        # Write the updated collection to the database file
        self.engine._save()

        print(f"Updated {len(data)} documents.")
        return len(data)
    
    # Delete from the collection
    def delete(self, query):
        print(f"Deleting data from collection '{self.name}' with query: {query}")

        # Find matching documents
        data = self.find(query)

        # If no documents match the query
        if not data:
            print("No documents matched the query. Nothing deleted.")
            return 0

        # 2. Get the full list from the engine
        raw_collection = self.engine.data[self.name]

        # 3. Remove each target from the full list by removing the items specified in the query
        for item in data:
            raw_collection.remove(item)

        # 4. Save the changes to the database file
        self.engine._save()

        print(f"Deleted {len(data)} documents.")
        return len(data)
