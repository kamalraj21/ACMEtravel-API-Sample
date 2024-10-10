from flask import Flask, jsonify, request, render_template, send_from_directory
from flasgger import Swagger
import os

app = Flask(__name__, template_folder='templates')

# Swagger configuration
swagger = Swagger(app)

# In-memory data stores
packages = []
hotels = []
customers = []

# Generic function for resource CRUD
def get_resource_by_id(resource_list, resource_id):
    return next((item for item in resource_list if item["id"] == resource_id), None)

def create_resource(resource_list, data):
    data['id'] = len(resource_list) + 1
    resource_list.append(data)
    return data

def update_resource(resource, data):
    resource.update(data)
    return resource

def delete_resource(resource_list, resource):
    resource_list.remove(resource)

# CRUD Endpoints for Packages
@app.route('/packages', methods=['GET'])
def get_packages():
    """
    Retrieve all vacation packages
    ---
    responses:
      200:
        description: A list of all vacation packages
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              name:
                type: string
              duration:
                type: string
              price:
                type: number
              description:
                type: string
    """
    return jsonify(packages)

@app.route('/packages', methods=['POST'])
def add_package():
    """
    Add a new vacation package
    ---
    parameters:
      - in: body
        name: body
        description: Vacation package details
        schema:
          type: object
          required:
            - name
            - duration
            - price
            - description
          properties:
            name:
              type: string
            duration:
              type: string
            price:
              type: number
            description:
              type: string
    responses:
      201:
        description: The created vacation package
    """
    new_package = create_resource(packages, request.get_json())
    return jsonify(new_package), 201

@app.route('/packages/<int:id>', methods=['GET'])
def get_package_by_id(id):
    """
    Retrieve a specific vacation package by ID
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: The requested vacation package
        schema:
          type: object
          properties:
            id:
              type: integer
            name:
              type: string
            duration:
              type: string
            price:
              type: number
            description:
              type: string
      404:
        description: Package not found
    """
    package = get_resource_by_id(packages, id)
    if package:
        return jsonify(package)
    return jsonify({"error": "Package not found"}), 404

@app.route('/packages/<int:id>', methods=['PUT'])
def update_package(id):
    """
    Update a vacation package by ID
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
      - in: body
        name: body
        description: Vacation package details to update
        schema:
          type: object
          required:
            - name
            - duration
            - price
            - description
          properties:
            name:
              type: string
            duration:
              type: string
            price:
              type: number
            description:
              type: string
    responses:
      200:
        description: The updated vacation package
      404:
        description: Package not found
    """
    package = get_resource_by_id(packages, id)
    if package:
        updated_package = update_resource(package, request.get_json())
        return jsonify(updated_package)
    return jsonify({"error": "Package not found"}), 404

@app.route('/packages/<int:id>', methods=['DELETE'])
def delete_package(id):
    """
    Delete a vacation package by ID
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      204:
        description: Package deleted
      404:
        description: Package not found
    """
    package = get_resource_by_id(packages, id)
    if package:
        delete_resource(packages, package)
        return jsonify({}), 204
    return jsonify({"error": "Package not found"}), 404

# CRUD Endpoints for Customers (similar to the Packages logic)
@app.route('/customers', methods=['GET'])
def get_customers():
    """
    Retrieve all customers
    ---
    responses:
      200:
        description: A list of all customers
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              name:
                type: string
              email:
                type: string
              phone:
                type: string
    """
    return jsonify(customers)

@app.route('/customers', methods=['POST'])
def add_customer():
    """
    Add a new customer
    ---
    parameters:
      - in: body
        name: body
        description: Customer details
        schema:
          type: object
          required:
            - name
            - email
          properties:
            name:
              type: string
            email:
              type: string
            phone:
              type: string
    responses:
      201:
        description: The created customer
    """
    new_customer = create_resource(customers, request.get_json())
    return jsonify(new_customer), 201

@app.route('/customers/<int:id>', methods=['GET'])
def get_customer_by_id(id):
    """
    Retrieve a customer by ID
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: The requested customer
        schema:
          type: object
          properties:
            id:
              type: integer
            name:
              type: string
            email:
              type: string
            phone:
              type: string
      404:
        description: Customer not found
    """
    customer = get_resource_by_id(customers, id)
    if customer:
        return jsonify(customer)
    return jsonify({"error": "Customer not found"}), 404

@app.route('/customers/<int:id>', methods=['PUT'])
def update_customer(id):
    """
    Update a customer by ID
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
      - in: body
        name: body
        description: Customer details to update
        schema:
          type: object
          required:
            - name
            - email
          properties:
            name:
              type: string
            email:
              type: string
            phone:
              type: string
    responses:
      200:
        description: The updated customer
      404:
        description: Customer not found
    """
    customer = get_resource_by_id(customers, id)
    if customer:
        updated_customer = update_resource(customer, request.get_json())
        return jsonify(updated_customer)
    return jsonify({"error": "Customer not found"}), 404

@app.route('/customers/<int:id>', methods=['DELETE'])
def delete_customer(id):
    """
    Delete a customer by ID
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      204:
        description: Customer deleted
      404:
        description: Customer not found
    """
    customer = get_resource_by_id(customers, id)
    if customer:
        delete_resource(customers, customer)
        return jsonify({}), 204
    return jsonify({"error": "Customer not found"}), 404

# Serve favicon.ico
@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico')

# Serve the home page
@app.route('/')
def serve_home():
    return render_template('index.html')

# Serve the OpenAPI JSON file
@app.route('/openapi.json')
def serve_openapi():
    return send_from_directory('.', 'openapi.json')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
