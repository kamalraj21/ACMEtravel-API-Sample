from flask import Flask, jsonify, request, send_from_directory
import os

app = Flask(__name__)

# Sample in-memory data store for packages
packages = []

# Serve the web interface
@app.route('/')
def serve_home():
    return send_from_directory('.', 'index.html')

# CRUD Endpoints for Vacation Packages
@app.route('/packages', methods=['GET'])
def get_packages():
    return jsonify(packages)

@app.route('/packages', methods=['POST'])
def add_package():
    new_package = request.get_json()
    new_package['id'] = len(packages) + 1
    packages.append(new_package)
    return jsonify(new_package), 201

@app.route('/packages/<int:package_id>', methods=['PUT'])
def update_package(package_id):
    package = next((p for p in packages if p['id'] == package_id), None)
    if package:
        updated_data = request.get_json()
        package.update(updated_data)
        return jsonify(package)
    else:
        return jsonify({'error': 'Package not found'}), 404

@app.route('/packages/<int:package_id>', methods=['DELETE'])
def delete_package(package_id):
    package = next((p for p in packages if p['id'] == package_id), None)
    if package:
        packages.remove(package)
        return jsonify({'message': 'Package deleted successfully'})
    else:
        return jsonify({'error': 'Package not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
