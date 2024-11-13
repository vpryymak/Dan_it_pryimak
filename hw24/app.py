import random
import string
from flask import Flask

app = Flask(__name__)

def generate_random_string(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route('/')
def home():
    return generate_random_string()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
