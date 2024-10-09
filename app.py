from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data to mimic a database
vacation_packages = [
    {
        "id": 1,
        "name": "Hawaii Beach Getaway",
        "duration": "7 days",
        "price": 2500,
        "description": "A week-long escape to the beautiful beaches of Hawaii."
    },
    {
        "id": 2,
        "name": "European Adventure",
        "duration": "14 days",
        "price": 4500,
        "description": "Explore the major cities of Europe in this two-week tour."
    },
    {
        "id": 3,
        "name": "Mysore Magic",
        "duration": "3 days",
        "price": 2500,
        "description": "Experience the magic of Mysore's heritage and hospitality."
    }

]

# Home route
@app.route('/', methods=['GET'])
def home():
    return "<h1>Welcome to ACME Travels API</h1><p>Use /packages to see available vacation packages.</p>"

# Favicon route to handle browser requests for favicon.ico
@app.route('/favicon.ico')
def favicon():
    return '', 204

# GET all vacation packages
@app.route('/packages', methods=['GET'])
def get_packages():
    return jsonify(vacation_packages)

# GET a specific vacation package by ID
@app.route('/packages/<int:package_id>', methods=['GET'])
def get_package(package_id):
    package = next((pkg for pkg in vacation_packages if pkg['id'] == package_id), None)
    if package:
        return jsonify(package)
    return jsonify({"error": "Package not found"}), 404

# CREATE a new vacation package
@app.route('/packages', methods=['POST'])
def create_package():
    new_package = request.get_json()
    new_package['id'] = len(vacation_packages) + 1
    vacation_packages.append(new_package)
    return jsonify(new_package), 201

# UPDATE an existing vacation package by ID
@app.route('/packages/<int:package_id>', methods=['PUT'])
def update_package(package_id):
    package = next((pkg for pkg in vacation_packages if pkg['id'] == package_id), None)
    if package:
        updated_data = request.get_json()
        package.update(updated_data)
        return jsonify(package)
    return jsonify({"error": "Package not found"}), 404

# DELETE a vacation package by ID
@app.route('/packages/<int:package_id>', methods=['DELETE'])
def delete_package(package_id):
    global vacation_packages
    vacation_packages = [pkg for pkg in vacation_packages if pkg['id'] != package_id]
    return jsonify({"message": "Package deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
