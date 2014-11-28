from app import app
from flask import render_template, request
from models import Todo

@app.route('/')
def index():
    todos = Todo.objects.all()
    return render_template("index.html", todos=todos)


@app.route('/add', methods=['POST', ])
def add():
    content = request.form.get("content")
    todo = Todo(content=content)
    todo.save()
    todos = Todo.objects.all()
    return render_template("index.html", todos=todos)