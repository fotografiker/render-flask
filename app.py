from flask import Flask, jsonify, request
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:3000/python"}})

@app.route('/')
def hello_world():
    message = {}
    data = {}
    
    message['message'] = 'Hello World from Flask!'
    data['status'] = 200
    data['data'] = message
    
    return jsonify(data)
if __name__ == '__main__':
    app.run(debug=True)