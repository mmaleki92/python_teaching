from flask import Flask, render_template, jsonify, request
import numpy as np
import pandas as pd
import json
from datetime import datetime, timedelta
import random

app = Flask(__name__)

# Generate mock data for the dashboard
def generate_sales_data(days=30):
    base = datetime.today() - timedelta(days=days)
    dates = [(base + timedelta(days=x)).strftime('%Y-%m-%d') for x in range(days)]
    
    products = ['Laptops', 'Phones', 'Tablets', 'Accessories', 'Services']
    regions = ['North', 'South', 'East', 'West']
    
    data = []
    for date in dates:
        for product in products:
            for region in regions:
                sales = round(random.uniform(100, 5000), 2)
                units = random.randint(1, 50)
                
                data.append({
                    'date': date,
                    'product': product,
                    'region': region,
                    'sales': sales,
                    'units': units
                })
    
    return data

# Global variable to store our mock data
SALES_DATA = generate_sales_data()

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/api/dashboard-summary')
def dashboard_summary():
    df = pd.DataFrame(SALES_DATA)
    
    # Calculate summary metrics
    total_sales = df['sales'].sum()
    total_units = df['units'].sum()
    avg_order_value = total_sales / len(df)
    
    # Product category breakdown
    product_sales = df.groupby('product')['sales'].sum().to_dict()
    
    # Regional performance
    regional_sales = df.groupby('region')['sales'].sum().to_dict()
    
    # Daily trend (last 7 days)
    recent_dates = sorted(df['date'].unique())[-7:]
    daily_trend = df[df['date'].isin(recent_dates)].groupby('date')['sales'].sum().to_dict()
    
    return jsonify({
        'total_sales': round(total_sales, 2),
        'total_units': int(total_units),
        'avg_order_value': round(avg_order_value, 2),
        'product_sales': product_sales,
        'regional_sales': regional_sales,
        'daily_trend': daily_trend
    })

@app.route('/api/sales-by-product')
def sales_by_product():
    df = pd.DataFrame(SALES_DATA)
    product_data = df.groupby('product').agg({
        'sales': 'sum',
        'units': 'sum'
    }).reset_index()
    
    return jsonify(product_data.to_dict(orient='records'))

@app.route('/api/sales-by-region')
def sales_by_region():
    df = pd.DataFrame(SALES_DATA)
    region_data = df.groupby('region').agg({
        'sales': 'sum',
        'units': 'sum'
    }).reset_index()
    
    return jsonify(region_data.to_dict(orient='records'))

@app.route('/api/daily-trend')
def daily_trend():
    df = pd.DataFrame(SALES_DATA)
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date')
    
    daily_data = df.groupby('date').agg({
        'sales': 'sum',
        'units': 'sum'
    }).reset_index()
    
    daily_data['date'] = daily_data['date'].dt.strftime('%Y-%m-%d')
    
    return jsonify(daily_data.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)