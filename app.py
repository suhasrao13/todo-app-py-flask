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

@app.route("/edit/<int:index>",methods=["GET","POST"])
def edit(index):
    todo=todos[index]
    if request.method=="POST":
        todo['task']=request.form['todo']
        return redirect(url_for("index"))
    else:
        return render_template('edit.html', todo=todo, index=index)