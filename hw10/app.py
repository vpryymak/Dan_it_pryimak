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

def generate_id(students):
    if not students:
        return 1
    return max(int(student[0]) for student in students) + 1

@app.route('/students', methods=['GET', 'POST'])
def students():
    if request.method == 'POST':
        data = request.get_json()
        if not data or 'first_name' not in data or 'last_name' not in data or 'age' not in data:
            return jsonify({'error': 'Missing fields'}), 400
        students = read_csv()
        id = generate_id(students)
        students.append([str(id), data['first_name'], data['last_name'], str(data['age'])])
        write_csv(students)
        return jsonify({'id': id, 'first_name': data['first_name'], 'last_name': data['last_name'], 'age': data['age']}), 201
    else:
        students = read_csv()
        # Return the data in a structured format
        return jsonify([{'id': s[0], 'first_name': s[1], 'last_name': s[2], 'age': s[3]} for s in students]), 200

def find_student_by_id(students, id):
    #Due to the headers in row 0 of students list, int function has not been working correctly. This is workaround
    students.pop(0)
    for student in students:
        if int(student[0]) == id:
            return student
    return None

@app.route('/students/<int:id>', methods=['GET', 'PUT', 'PATCH', 'DELETE'])
def student(id):
    students = read_csv()
    student = find_student_by_id(students, id)
    if not student:
        return jsonify({'error': 'Student not found'}), 404

    if request.method == 'GET':
        return jsonify({'id': student[0], 'first_name': student[1], 'last_name': student[2], 'age': student[3]}), 200
    elif request.method == 'DELETE':
        students.remove(student)
        write_csv(students)
        return jsonify({'success': 'Student deleted'}), 200
    else:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No fields to update'}), 400
        if request.method == 'PUT' or request.method == 'POST':  # Assuming POST is used like PUT
            if 'first_name' not in data or 'last_name' not in data or 'age' not in data:
                return jsonify({'error': 'Missing fields'}), 400
            student[1] = data['first_name']
            student[2] = data['last_name']
            student[3] = data['age']
        elif request.method == 'PATCH':
            if 'age' in data:
                student[3] = data['age']
        write_csv(students)
        return jsonify({'id': student[0], 'first_name': student[1], 'last_name': student[2], 'age': student[3]}), 200


if __name__ == '__main__':
    app.run(debug=True)
