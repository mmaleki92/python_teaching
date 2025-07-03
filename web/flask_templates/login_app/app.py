from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Simple in-memory user storage (in a real app, use a database)
users = {}

@app.route('/')
def home():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in users:
            flash('Username already exists!')
            return redirect(url_for('register'))
        
        users[username] = {
            'password': generate_password_hash(password),
            'name': request.form['name']
        }
        
        flash('Registration successful! Please login.')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username not in users:
            flash('Invalid username or password!')
            return redirect(url_for('login'))
        
        if check_password_hash(users[username]['password'], password):
            session['user_id'] = username
            flash(f'Welcome back, {users[username]["name"]}!')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password!')
    
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Please login first!')
        return redirect(url_for('login'))
    
    user = users[session['user_id']]
    return render_template('dashboard.html', user=user)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out!')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)