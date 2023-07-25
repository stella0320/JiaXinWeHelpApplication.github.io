from flask import Flask
from flask import render_template

app = Flask(__name__, static_url_path="/")


@app.route('/login')
def login():
    return render_template('/login.html')


app.run(port=3000)