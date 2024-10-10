from flask import Flask, jsonify, request

# Create an instance of the Flask class
app = Flask(__name__)

# Sample data for vacation packages
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
    }
]

# Home route
@app.route('/')
def home():
    return "<h1>Welcome to ACME Travels API</h1><p>Use /packages to see available vacation packages.</p>"

# Get all vacation packages
@app.route('/packages', methods=['GET'])
def get_packages():
    return jsonify(vacation_packages)

# Get a specific vacation package by ID
@app.route('/packages/<int:package_id>', methods=['GET'])
def get_package(package_id):
    package = next((p for p in vacation_packages if p["id"] == package_id), None)
    if package:
        return jsonify(package)
    else:
        return jsonify({"error": "Package not found"}), 404

# Create a new vacation package
@app.route('/packages', methods=['POST'])
def create_package():
    new_package = request.get_json()
    new_package["id"] = len(vacation_packages) + 1
    vacation_packages.append(new_package)
    return jsonify(new_package), 201

# Update an existing vacation package
@app.route('/packages/<int:package_id>', methods=['PUT'])
def update_package(package_id):
    package = next((p for p in vacation_packages if p["id"] == package_id), None)
    if package:
        data = request.get_json()
        package.update(data)
        return jsonify(package)
    else:
        return jsonify({"error": "Package not found"}), 404

# Delete a vacation package
@app.route('/packages/<int:package_id>', methods=['DELETE'])
def delete_package(package_id):
    package = next((p for p in vacation_packages if p["id"] == package_id), None)
    if package:
        vacation_packages.remove(package)
        return jsonify({"message": "Package deleted successfully"}), 200
    else:
        return jsonify({"error": "Package not found"}), 404

# Entry point for local testing
if __name__ == "__main__":
    # Define a default port
    port = 5000
    app.run(host="0.0.0.0", port=port)
