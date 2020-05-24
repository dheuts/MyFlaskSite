from flask import Flask, render_template

app = Flask(__name__)

all_posts = [
    {
        'title': 'Post 1',
        'content': 'This is the content of Post 1',
        'author': 'David'
    },
    {
        'title': 'Post 2',
        'content': 'This is the content of Post 2'
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts')
def posts():
    return render_template('posts.html', posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)