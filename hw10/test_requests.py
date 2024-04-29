import requests
import json

def write_to_file(data):
    with open('results.txt', 'a') as f:
        f.write(json.dumps(data, indent=4))
        f.write('\n')

base_url = 'http://localhost:5000/students'

# Retrieve all existing students (GET)
response = requests.get(base_url)
print(response.json())
write_to_file(response.json())

# Create three students (POST)
students = [
    {"first_name": "John", "last_name": "Doe", "age": 20},
    {"first_name": "Jane", "last_name": "Doe", "age": 22},
    {"first_name": "Jim", "last_name": "Smith", "age": 21}
]
for student in students:
    response = requests.post(base_url, json=student)
    print(response.json())
    write_to_file(response.json())

# Retrieve information about all existing students (GET)
response = requests.get(base_url)
print(response.json())
write_to_file(response.json())

# Update the age of the second student (PATCH)
response = requests.patch(f'{base_url}/2', json={"age": 23})
print(response.json())
write_to_file(response.json())

# Retrieve information about the second student (GET)
response = requests.get(f'{base_url}/2')
print(response.json())
write_to_file(response.json())

# Update the first name, last name and the age of the third student (PUT)
response = requests.put(f'{base_url}/3', json={"first_name": "James", "last_name": "Johnson", "age": 24})
print(response.json())
write_to_file(response.json())

# Retrieve information about the third student (GET)
response = requests.get(f'{base_url}/3')
print(response.json())
write_to_file(response.json())

# Retrieve all existing students (GET)
response = requests.get(base_url)
print(response.json())
write_to_file(response.json())

# Delete the first user (DELETE)
response = requests.delete(f'{base_url}/1')
print(response.json())
write_to_file(response.json())

# Retrieve all existing students (GET)
response = requests.get(base_url)
print(response.json())
write_to_file(response.json())
