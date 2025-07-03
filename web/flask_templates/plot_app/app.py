from flask import Flask, render_template, jsonify
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

app = Flask(__name__)

# Generate sample stock data
def generate_stock_data(days=30):
    base = datetime.today() - timedelta(days=days)
    dates = [base + timedelta(days=x) for x in range(days)]
    date_strings = [date.strftime('%Y-%m-%d') for date in dates]
    
    # Generate prices with some random walk behavior
    prices = [100]  # Start at $100
    for i in range(1, days):
        change = np.random.normal(0, 1)  # Random daily change
        new_price = max(0.1, prices[-1] * (1 + change/100))  # Ensure price stays positive
        prices.append(round(new_price, 2))
    
    return {
        'dates': date_strings,
        'prices': prices
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/stock-data')
def stock_data():
    data = generate_stock_data(days=30)
    return jsonify(data)

@app.route('/api/histogram-data')
def histogram_data():
    # Generate random data for histogram
    data = np.random.normal(0, 1, 1000).tolist()
    return jsonify({'data': data})

@app.route('/api/pie-data')
def pie_data():
    categories = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']
    values = [np.random.randint(10, 100) for _ in range(len(categories))]
    return jsonify({'categories': categories, 'values': values})

if __name__ == '__main__':
    app.run(debug=True)