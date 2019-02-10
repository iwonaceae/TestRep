
from flask import Flask, render_template, make_response
import json

# Initialize the app
app = Flask(__name__)

# Hardcoded values
numbers_to_add = list(range(10000001))

# Function to calculate sum
def add_numbers(numbers_to_add):
    total = sum(numbers_to_add)
    return total

# Total directory
@app.route("/total")
def total():
    total = add_numbers(numbers_to_add)
    result = json.dumps({"total": total},sort_keys=False, indent=4)
    rendered = render_template('total.json', result = result)
    resp = make_response(rendered)
    resp.mimetype = "application/json"
    return resp

# run server (by default on port 5000)
if __name__ == '__main__':
    app.run(debug=True)