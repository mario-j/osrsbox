  
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager

from flask_script import Manager
from flask_migrate import ( Migrate, MigrateCommand )

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

login_manager = LoginManager()

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    complete = db.Column(db.Boolean)
    quantity = db.Column(db.Integer)
    buy = db.Column(db.Integer)
    sell = db.Column(db.Integer)

@app.route('/')
def index():
    incomplete = Todo.query.filter_by(complete=False).all()
    complete = Todo.query.filter_by(complete=True).all()

    return render_template('index.html', incomplete=incomplete, complete=complete)

@app.route('/add', methods=['POST'])
def add():
    todo = Todo(text=request.form['todoitem'], quantity=request.form['itemquantity'], buy=request.form['itembuyprice'], sell=request.form['itemsellprice'], complete=False)
    db.session.add(todo)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/search', methods=['POST'])
def search():

    search = request.form.get('search')
    todo_list = db.session.query(Todo).filter(Todo.text.like("%" + search + "%")).all()
    return render_template('search.html', todo_list=todo_list )

@app.route('/complete/<id>')
def complete(id):

    todo = Todo.query.filter_by(id=int(id)).first()
    todo.complete = True
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/delete/<id>')
def delete(id):

    todo = Todo.query.filter_by(id=int(id)).delete()
    db.session.commit()

    return redirect('/')

if __name__ == '__main__':
    manager.run()
    # app.run(debug=True)