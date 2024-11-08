import sqlite3
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

#define routes
from flask import Flask, render_template, request, jsonify
import pandas as pd

@app.route('/get_chart', methods=['POST'])
def get_chart():
    # Extract data from form
    symbol = request.form['symbol']
    # Query Alpha Vantage API here and generate chart (use existing code from project 3)
    # Return chart data to render on the webpage
    return render_template('index.html', chart_data=chart_data)

app.run(host="0.0.0.0")
