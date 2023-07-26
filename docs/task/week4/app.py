from datetime import timedelta
import os
from flask import Flask, url_for
from flask import render_template
from flask import request
from flask import redirect
from flask import session
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=1)

@app.route('/')
def login():
    if session.get('signed_in'):
        return redirect('/member')
    return render_template('/login.html', time=str(time.time()))

@app.route('/error')
def error():
    msg = request.args.get("msg", "")
    return render_template('/errorPage.html', error=msg, time=str(time.time()))

@app.route('/member')
def member():
    if not session.get('signed_in'):
        return redirect('/')
    return render_template('/member.html', time=str(time.time()))

@app.route('/signout')
def signout():
    # 登出後，將session移除
    if session.get('signed_in'):
        session['signed_in'] = False
    return redirect('/')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    if not username or not password:
        # 帳號或密碼為空
        return redirect(url_for('error', msg = "Please enter username and password"))
    elif username != 'test' or password != 'test':
        # 帳號或密碼錯誤
        return redirect(url_for('error', msg = "Username or password is not correct"))
    
    if username:
        # 新增session
        session['signed_in'] = True
    return redirect('/member')

app.run(port=3000)

# https://flask.palletsprojects.com/en/2.3.x/tutorial/layout/