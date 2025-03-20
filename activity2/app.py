from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Sample data
items = [
    {"id": 1, "name": "earbuds", "price": 999},
    {"id": 2, "name": "marie", "price": 750},
    {"id": 3, "name": "yanong", "price": 690}
]

#Endpoint: Welcome message
@app.route('/', methods=['GET'])
def welcome():
    return jsonify({"message": "Welcome to the Flask API!"})

#Endpoint: Get list of items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify({"items": items})

#Endpoint: Get item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({"error": "Item not found"}), 404

#Endpoint: Add a new item (POST request)
@app.route('/api/items', methods=['POST'])
def add_item():
    data = request.get_json()
    new_item = {
        "id": len(items) + 1,
        "name": data['name'],
        "price": data['price']
    }
    items.append(new_item)
    return jsonify(new_item), 201

#Render items on an HTML page using Jinja2
@app.route('/items/html')
def show_items():
    return render_template('index.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)
