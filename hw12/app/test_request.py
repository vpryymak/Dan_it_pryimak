import requests
import json


def write_to_file(data):
    with open('results.txt', 'a') as f:
        f.write(json.dumps(data, indent=4))
        f.write('\n')


base_url = 'http://127.0.0.1:5000/students'


def print_write(data):
    print(f'Response is {data}')
    write_to_file(data)


# Retrieve all existing students (GET)
response = requests.get(base_url)
print_write(response.json())


# Create three students (POST)
students = [
    {"first_name": "John", "last_name": "Doe", "age": 20},
    {"first_name": "Jane", "last_name": "Doe", "age": 22},
    {"first_name": "Jim", "last_name": "Smith", "age": 21}
]


#USe try/except
for student in students:
    try:
        # Add try/except
        response = requests.post(base_url, json=student)
        print_write(response.json())
    except Exception as e:
        print(f"Error: {e}")

    try:
        # Retrieve information about all existing students (GET)
        response = requests.get(base_url)
        print_write(response.json())
    except Exception as e:
        print(f"Error: {e}")

    try:
        # Update the age of the second student (PATCH)
        response = requests.patch(f'{base_url}/2', json={"age": 23})
        print_write(response.json())
    except Exception as e:
        print(f"Error: {e}")

    try:
        # Retrieve information about the second student (GET)
        response = requests.get(f'{base_url}/2')
        print_write(response.json())
    except Exception as e:
        print(f"Error: {e}")

    try:
        # Update the first name, last name and the age of the third student (PUT)
        response = requests.put(f'{base_url}/3', json={"first_name": "James", "last_name": "Johnson", "age": 24})
        print_write(response.json())
    except Exception as e:
        print(f"Error: {e}")

    try:
        # Retrieve information about the third student (GET)
        response = requests.get(f'{base_url}/3')
        print_write(response.json())
    except Exception as e:
        print(f"Error: {e}")
