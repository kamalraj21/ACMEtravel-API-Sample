# ACME Travels API - Vacation Packages

This is a sample REST API for managing vacation packages for ACME Travels. The API allows users to perform CRUD (Create, Read, Update, Delete) operations on vacation packages.

## Getting Started

### Prerequisites
- **Python 3.7+**
- **Flask** library

To install Flask, run:
```sh
pip install Flask
```

### Running the API
1. Clone the repository:
   ```sh
   git clone https://github.com/kamalraj21/ACMEtravel-API-Sample.git
   cd ACMEtravel-API-Sample
   ```

2. Run the server:
   ```sh
   python app.py
   ```

3. The server will start on `http://127.0.0.1:5000/`.

### Deploying the API
To deploy the ACME Travels API, you can use a cloud service like **Heroku**, **Render**, or **AWS**. Below are instructions for deploying on **Heroku** as an example.

#### Deploying on Heroku

1. **Install Heroku CLI**:
   - Visit [Heroku CLI installation page](https://devcenter.heroku.com/articles/heroku-cli) and follow the installation instructions.

2. **Prepare the Project for Deployment**:
   - Create a `requirements.txt` file to specify dependencies:
     ```sh
     pip freeze > requirements.txt
     ```
   - Create a `Procfile` to define how to run the application:
     ```
     web: python app.py
     ```

3. **Initialize a Git Repository** (if not already done):
   ```sh
   git init
   git add .
   git commit -m "Initial commit"
   ```

4. **Create a Heroku App**:
   ```sh
   heroku login
   heroku create acmetravel-api-sample
   ```

5. **Deploy to Heroku**:
   ```sh
   git push heroku main
   ```

6. **Access the Deployed API**:
   - Once deployment is complete, you can access the API using the URL provided by Heroku (e.g., `https://acmetravel-api-sample.herokuapp.com/`).

### Deploying on Render

1. **Create an Account**:
   - Visit [Render's website](https://render.com) and create an account.

2. **Create a New Web Service**:
   - Select **New +** > **Web Service**.
   - Connect your GitHub repository and select the branch to deploy.

3. **Configure Build and Start Command**:
   - Build command: `pip install -r requirements.txt`
   - Start command: `python app.py`

4. **Deploy**:
   - Click **Deploy** and wait for Render to build and deploy your service.

### Deploying on AWS (Elastic Beanstalk)

1. **Install AWS Elastic Beanstalk CLI**:
   - Follow the instructions [here](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install.html) to install the EB CLI.

2. **Initialize Elastic Beanstalk Application**:
   ```sh
   eb init -p python-3.7 acmetravel-api-sample
   eb create acmetravel-env
   ```

3. **Deploy**:
   ```sh
   eb deploy
   ```

4. **Access the API**:
   - You can access the API using the environment URL provided by AWS.

### Testing the API
You can use **Postman**, **cURL**, or simply your browser to test the endpoints.

## API Endpoints

### 1. Home
- **URL**: `/`
- **Method**: `GET`
- **Description**: Displays a welcome message and a brief description of available endpoints.
- **Response**:
  ```html
  <h1>Welcome to ACME Travels API</h1>
  <p>Use /packages to see available vacation packages.</p>
  ```

### 2. Get All Vacation Packages
- **URL**: `/packages`
- **Method**: `GET`
- **Description**: Fetch all available vacation packages.
- **Response**:
  ```json
  [
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
  ```

### 3. Get a Specific Vacation Package
- **URL**: `/packages/<package_id>`
- **Method**: `GET`
- **Description**: Fetch details of a specific vacation package by ID.
- **Parameters**:
  - `package_id` (int): ID of the vacation package.
- **Response** (Example for ID 1):
  ```json
  {
    "id": 1,
    "name": "Hawaii Beach Getaway",
    "duration": "7 days",
    "price": 2500,
    "description": "A week-long escape to the beautiful beaches of Hawaii."
  }
  ```

### 4. Create a New Vacation Package
- **URL**: `/packages`
- **Method**: `POST`
- **Description**: Add a new vacation package.
- **Request Body**:
  ```json
  {
    "name": "Anjuna Sunsets",
    "duration": "5 days",
    "price": 2500,
    "description": "Enjoy the Goan Fish curry and beautiful sunsets."
  }
  ```
- **Response**:
  ```json
  {
    "id": 3,
    "name": "Anjuna Sunsets",
    "duration": "5 days",
    "price": 2500,
    "description": "Enjoy the Goan Fish curry and beautiful sunsets."
  }
  ```

### 5. Update an Existing Vacation Package
- **URL**: `/packages/<package_id>`
- **Method**: `PUT`
- **Description**: Update details of an existing vacation package.
- **Parameters**:
  - `package_id` (int): ID of the vacation package to update.
- **Request Body** (Example to update the price):
  ```json
  {
    "price": 2600
  }
  ```
- **Response** (Updated package):
  ```json
  {
    "id": 1,
    "name": "Hawaii Beach Getaway",
    "duration": "7 days",
    "price": 2600,
    "description": "A week-long escape to the beautiful beaches of Hawaii."
  }
  ```

### 6. Delete a Vacation Package
- **URL**: `/packages/<package_id>`
- **Method**: `DELETE`
- **Description**: Delete a vacation package by ID.
- **Parameters**:
  - `package_id` (int): ID of the vacation package to delete.
- **Response**:
  ```json
  {
    "message": "Package deleted successfully"
  }
  ```

## Sample Data
- The API starts with the following pre-defined vacation packages:
  1. **Hawaii Beach Getaway**: 7 days, $2500
  2. **European Adventure**: 14 days, $4500

## Notes
- This API is a development server and should **not** be used in a production environment. For production deployment, use a production WSGI server (e.g., Gunicorn).
- **Favicon Warning**: A `favicon.ico` route has been added to handle browser requests for a favicon.

## Contributing
Feel free to submit pull requests or issues for further improvement.

## License
This project is licensed under the MIT License.

---

### Happy Travels with ACME!
