
from os import times
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

import generating
#x = generating.generating()
app = Flask(__name__)
app.static_folder = 'static'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sudoku'
db = SQLAlchemy(app)

class Sudoku(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Sudoku = db.Column(db.String(200), nullable=False)
    times = db.column(db.String(20))

    def __repr__(self):
        return "Name" + self.id

@app.route("/app")
def fun():
    text = generating.generating()
    return render_template('sample.html', sat = text)

if __name__ == "__main__" :
    #app.run(host="0.0.0.0")
    app.run()