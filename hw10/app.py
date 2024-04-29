from flask import Flask, request, jsonify
import csv
import os

app = Flask(__name__)

def read_csv():
    if not os.path.exists('students.csv'):
        return []
    with open('students.csv', 'r') as f:
        return list(csv.reader(f))

def write_csv(data):
    with open('students.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)

@app.route('/students', methods=['GET', 'POST'])
def students():
    if request.method == 'POST':
        data = request.get_json()
        if not data or 'first_name' not in data or 'last_name' not in data or 'age' not in data:
            return jsonify({'error': 'Missing fields'}), 400
        students = read_csv()
        id = len(students) + 1
        students.append([id, data['first_name'], data['last_name'], data['age']])
        write_csv(students)
        return jsonify({'id': id, 'first_name': data['first_name'], 'last_name': data['last_name'], 'age': data['age']}), 201
    else:
        students = read_csv()
        return jsonify(students), 200

@app.route('/students/<int:id>', methods=['GET', 'PUT', 'PATCH', 'DELETE'])
def student(id):
    students = read_csv()
    student = next((s for s in students if int(s[0]) == id), None)
    if not student:
        return jsonify({'error': 'Student not found'}), 404

    if request.method == 'GET':
        return jsonify(student), 200
    elif request.method == 'DELETE':
        students.remove(student)
        write_csv(students)
        return jsonify({'success': 'Student deleted'}), 200
    else:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No fields to update'}), 400
        if request.method == 'PUT':
            if 'first_name' not in data or 'last_name' not in data or 'age' not in data:
                return jsonify({'error': 'Missing fields'}), 400
            student[1] = data['first_name']
            student[2] = data['last_name']
            student[3] = data['age']
        elif request.method == 'PATCH':
            if 'age' not in data:
                return jsonify({'error': 'Missing age field'}), 400
            student[3] = data['age']
        write_csv(students)
        return jsonify(student), 200

if __name__ == '__main__':
    app.run(debug=True)
