import json as j

with open("D:\\Python\\jsonworking\\Json_File.json","r") as f:
    # Load JSON data from the file into a Python dictionary
    Py_Dict_Data = j.load(f)
print(Py_Dict_Data)

with open("D:\\Python\\jsonworking\\Json_File1.json","w") as f:
    # Write the Python dictionary back to a JSON file with indentation for readability
    j.dump(Py_Dict_Data, f, indent=10)


json_string = '''
{
  "name": "Alice",
  "age": 30,
  "email": "alice@example.com",
  "is_active": true,
  "roles": ["admin", "editor"]
}
'''

# Convert JSON string into a Python dictionary
# This is useful for working with JSON data in Python
# using Python's native data structures

data = j.loads(json_string)

# Convert the Python dictionary back into a JSON string
# with indentation for better readability
json_stringanother = j.dumps(data, indent=4)
print(json_stringanother)
