from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Sample task data
tasks = []

# Route for the Welcome Page (Page 1)
@app.route('/')
def welcome():
    return render_template('welcome.html')

# Route for the Task Creation Page (Page 2)
@app.route('/task_page', methods=['GET', 'POST'])
def task_page():
    if request.method == 'POST':
        task_name = request.form.get('task')
        priority = request.form.get('priority')
        deadline = request.form.get('deadline')
        tasks.append({'task': task_name, 'priority': priority, 'deadline': deadline, 'completed': False})
        return redirect(url_for('task_list'))
    return render_template('task_page.html', tasks=sorted(tasks, key=lambda x: (x['priority'], x['deadline'])))

# Route for the Task Display Page (Page 3)
@app.route('/task_list')
def task_list():
    return render_template('task_list.html', tasks=tasks)

if __name__ == "__main__":
    app.run(debug=True)
