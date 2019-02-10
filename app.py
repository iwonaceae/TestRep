
from flask import Flask
from flask import jsonify

# Initialize the app
app = Flask(__name__)

# Total directory
@app.route("/total")
def result():
    
    # Hardcoded values
    numbers_to_add = list(range(10000001))
    result = sum(numbers_to_add)
    return jsonify({'total': result})

# Run server (by default on port 5000)
if __name__ == '__main__':
    app.run(debug=True)