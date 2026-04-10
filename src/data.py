import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(BASE_DIR, './data/data.json')

try:
    with open(json_path, 'r') as file:
        book_data = json.load(file)
    
except FileNotFoundError:
    print("Error: The file 'data.json' was not found.")


serial = book_data['book']
for x in serial:
    print(x['id'])

# print(serial)
# print(book_data = json.dumps(data, indent=4))