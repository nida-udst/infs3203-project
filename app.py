from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from models import db, Library
from forms import QuestionForm
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///self-assessment.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Initialize database
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/question-library')
def getLibrary():
    library = Library.query.all()
    return render_template('Library.html', library=library)

@app.route('/api/question-library', methods=['GET'])
def get_questions():
    library = Library.query.all()
    return jsonify([library.to_dict() for question in library])

if __name__ == '__main__':
    app.run(debug=True, port=5001)
