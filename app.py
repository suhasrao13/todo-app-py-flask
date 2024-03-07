from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__,template_folder='templates')

todos=[{"task": "simpletodo","done":False}]

@app.route('/')
def index():
    return render_template('index.html',todos=todos)

@app.route("/add",methods=["POST"])
def add():
    todo=request.form['todo']
    todos.append({"task":todo,"done":False})
    return redirect(url_for("index"))