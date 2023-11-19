# app.py
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://mongo:27017/crud_app'
mongo = PyMongo(app)

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    name = data.get('name')
    age = data.get('age')

    if name and age:
        user = {'name': name, 'age': age}
        mongo.db.users.insert_one(user)
        return jsonify({'message': 'User added successfully'}), 201
    else:
        return jsonify({'error': 'Missing data'}), 400

@app.route('/get', methods=['GET'])
def get_all():
    users = mongo.db.users.find()
    user_list = [{'name': user['name'], 'age': user['age']} for user in users]
    return jsonify({'users': user_list})

@app.route('/update/<name>', methods=['PUT'])
def update(name):
    data = request.get_json()
    new_age = data.get('age')

    if new_age:
        mongo.db.users.update_one({'name': name}, {'$set': {'age': new_age}})
        return jsonify({'message': 'User updated successfully'})
    else:
        return jsonify({'error': 'Missing data'}), 400

@app.route('/delete/<name>', methods=['DELETE'])
def delete(name):
    mongo.db.users.delete_one({'name': name})
    return jsonify({'message': 'User deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
