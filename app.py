from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

toDoList = ["test1", "test2", "test3"]

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', toDoList=toDoList)

@app.route('/add', methods=['POST'])
def add():
    item = request.form['item']
    toDoList.append(item)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)