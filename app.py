from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
tasks = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task = request.form.get('task')
        if task:
            tasks.append(task)
        return redirect(url_for('index'))
    return render_template('index.html', tasks=tasks)

@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit(index):
    if index >= len(tasks):
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        new_task = request.form.get('task')
        if new_task:
            tasks[index] = new_task
        return redirect(url_for('index'))
    
    return render_template('edit.html', index=index, task=tasks[index])

@app.route('/delete/<int:index>', methods=['POST'])
def delete(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)
