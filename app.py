
from flask import Flask, request, jsonify, send_from_directory
import mysql.connector

app = Flask(__name__,static_folder='public',static_url_path='/p1')

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password",
    database="restaurant_db"
)

@app.route('/p1')
def home():
    return send_from_directory('public', 'index.html')

@app.route('/api/menu', methods=['GET'])
def get_menu():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM menu")
    result = cursor.fetchall()
    return jsonify(result)

@app.route('/api/menu', methods=['POST'])
def add_item():
    data = request.json
    cursor = db.cursor()
    cursor.execute("INSERT INTO menu (name, price) VALUES (%s, %s)", (data['name'], data['price']))
    db.commit()
    return jsonify({"message": "Item added"})

@app.route('/api/menu/<int:id>', methods=['PUT'])
def update_item(id):
    data = request.json
    cursor = db.cursor()
    cursor.execute("UPDATE menu SET name=%s, price=%s WHERE id=%s", (data['name'], data['price'], id))
    db.commit()
    return jsonify({"message": "Item updated"})

@app.route('/api/menu/<int:id>', methods=['DELETE'])
def delete_item(id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM menu WHERE id=%s", (id,))
    db.commit()
    return jsonify({"message": "Item deleted"})

if __name__ == '__main__':
    app.run(debug=True)
