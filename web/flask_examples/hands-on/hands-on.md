# Exercise 1: Hello Flask


```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_flask():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run(debug=True)

```

# Exercise 2: Dynamic Route

```python
from flask import Flask

app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
    return f'Hello, {name}!'
```

# Exercise 3: HTML Templates

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name_template(name):
    return render_template('greeting.html', name=name)

```

`greeting.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Greeting</title>
</head>
<body>
    <h1>Hello, {{ name }}!</h1>
</body>
</html>
```

# Exercise 4: Form Handling

```python
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        name = request.form['name']
        return render_template('greeting.html', name=name)
    return render_template('greet_form.html')
```

`greet_form.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Greet Form</title>
</head>
<body>
    <form method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <input type="submit" value="Greet">
    </form>
</body>
</html>
```

# Exercise 5: Data Storage

```python
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

db.create_all()

@app.route('/posts')
def display_posts():
    posts = Post.query.all()
    return render_template('posts.html', posts=posts)

```
`posts.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog Posts</title>
</head>
<body>
    <h2>Blog Posts</h2>
    <ul>
        {% for post in posts %}
            <li>{{ post.title }}</li>
        {% endfor %}
    </ul>
</body>
</html>

```

# Exercise 6: Display Blog Posts

```python
# Add to the previous code
@app.route('/posts')
def display_posts():
    posts = Post.query.all()
    return render_template('posts.html', posts=posts)

```

# Exercise 7: Individual Blog Post
```python
# Add to the previous code
@app.route('/post/<int:post_id>')
def display_post(post_id):
    post = Post.query.get(post_id)
    return render_template('post.html', post=post)
```
`post.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ post.title }}</title>
</head>
<body>
    <h2>{{ post.title }}</h2>
    <p>{{ post.content }}</p>
</body>
</html>
```
