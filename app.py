from flask import Flask, render_template, request, redirect, url_for, flash
import redis

app = Flask(__name__)
app.secret_key = 'your_secret_key'

redis_client = redis.StrictRedis(host='redis', port=6379, db=0, decode_responses=True)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    stored_password = redis_client.hget('users', username)

    if stored_password and stored_password == password:
        return f"Welcome {username}!"
    else:
        flash('Invalid username or password', 'error')
        return redirect(url_for('home'))

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']

    if redis_client.hexists('users', username):
        flash('Username already exists!', 'error')
        return redirect(url_for('home'))

    redis_client.hset('users', username, password)

    flash('Registration successful! Please log in.', 'success')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')