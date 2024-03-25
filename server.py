from flask import Flask, jsonify
from flask_cors import CORS  # Import the CORS middleware

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

PORT = int(os.environ.get('PORT', 5000))  # Use the provided port or default to 5000

# Sample data
cafe_data = {
    "name": "Cafe Z",
    "location": "London, UK",
    "contact": "+44-12-12345678",
    "hours": {
        "weekdays": "6:00am - 6:00pm",
        "saturday": "7:00am - 7:00pm",
        "sunday": "Closed"
    }
}

# Route to handle GET requests to the root endpoint
@app.route('/')
def get_cafe_data():
    return jsonify(cafe_data)

# Start the server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
