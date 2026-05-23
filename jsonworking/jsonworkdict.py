import json

json_data_string = """
{
    "users": [
        {"id": 1, "name": "Amit", "friends": [2, 3], "liked_pages": [101]},
        {"id": 2, "name": "Priya", "friends": [1, 4], "liked_pages": [102]},
        {"id": 3, "name": "Rahul", "friends": [1], "liked_pages": [101, 103]},
        {"id": 4, "name": "Sara", "friends": [2], "liked_pages": [104]}
    ],
    "pages": [
        {"id": 101, "name": "Python Developers"},
        {"id": 102, "name": "Data Science Enthusiasts"},
        {"id": 103, "name": "AI & ML Community"},
        {"id": 104, "name": "Web Dev Hub"}
    ]
}
"""

# Convert the JSON string to a Python dictionary
data = json.loads(json_data_string)

print("--- Original Python Dictionary Structure ---")
print(type(data)) # Should be <class 'dict'>
print(data.keys()) # Shows the top-level keys
# Access the 'users' list
users_list = data['users']
print(f"Type of users_list: {type(users_list)}")
print(f"Number of users: {len(users_list)}")

# Access the 'pages' list
pages_list = data['pages']
print(f"Type of pages_list: {type(pages_list)}")
print(f"Number of pages: {len(pages_list)}")

print("-" * 40)