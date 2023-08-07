from datetime import timedelta
import os
from flask import Flask, url_for
from flask import render_template
from flask import request
from flask import redirect
from flask import session
import time
import random
from website import Website

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=1)

@app.route('/')
def login():
    # print('login:'+ request.cookies.get(app.config['SESSION_COOKIE_NAME']))
    if session.get('signed_in'):
        return redirect('/member')
    return render_template('/login.html', time=str(time.time()))

@app.route('/error')
def error():
    message = request.args.get("message", "")
    return render_template('/errorPage.html', error=message, time=str(time.time()))

@app.route('/member')
def member():
    # 紀錄session
    print('member:'+request.cookies.get(app.config['SESSION_COOKIE_NAME']))
    member = session.get('signed_in')
    if not member:
        return redirect('/')
    return render_template('/member.html', time=str(time.time()), name = member['name'])

@app.route('/signout')
def signout():
    # 登出後，將session移除
    if session.get('signed_in'):
        session['signed_in'] = False
    return redirect('/')

@app.route('/registration', methods = ['POST'])
def registration():
    if session.get('signed_in'):
        return redirect('/member')
   
    username = request.form.get('username', '')
    db_connect = Website('localhost', 'root', 'root')
    member = db_connect.queryMemberByUserName(username)

    if member:
        return redirect(url_for('error', message = "帳號已經被註冊"))
    
    password = request.form.get('password', '')
    name = request.form.get('username', '')
    db_connect.insertNewMember(name, username, password)
    member = db_connect.queryMemberByUserName(username)
    session['signed_in'] = member
    return redirect('/member')


@app.route('/signin', methods = ['POST'])
def signin():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    if not username or not password:
        # 帳號或密碼為空
        return redirect(url_for('error', message = "Please enter username and password"))
    
    
    db_connect = Website('localhost', 'root', 'root')
    member = db_connect.queryMemberByUserName(username)
    if not member or member['password'] != password:
        # 帳號或密碼錯誤
        return redirect(url_for('error', message = "Username or password is not correct"))
    
    if username:
        # 新增session
        session['signed_in'] = member
    return redirect('/member')


app.run(port=3000)

# https://flask.palletsprojects.com/en/2.3.x/tutorial/layout/