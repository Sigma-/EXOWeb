from flask import Flask

from flask import render_template, redirect
from flask import url_for, request

app = Flask(__name__)

tasks = ["task1", "task2"]

@app.route('/')
def index():
        return "Hello world !"

@app.route('/tasks')
def show_tasks(task=""):
	if task:
		tasks.append(task)

	return render_template('process_form.html', tasks=tasks)


@app.route('/process_request', methods=['POST'])
def process_request():
	if request.method == 'POST':
		_task = request.form.get("task")
		if _task:
			return show_tasks(_task)
		else:
			return 'Go back', 400

	else:
		return render_template('process_form.html', form=form)

@app.route('/delete', methods=['GET'])
def delete():



