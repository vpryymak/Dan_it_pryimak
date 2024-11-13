from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Connect to the MySQL database
def get_db_connection():
    conn = mysql.connector.connect(
        host='mysql',  # MySQL container name in Docker (configured later)
        user='root',
        password='root_password',
        database='app_db'
    )
    return conn

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name, email) VALUES (%s, %s)', (name, email))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'User added successfully'}), 201

@app.route('/get_users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return jsonify(users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
