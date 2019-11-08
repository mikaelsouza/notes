from flask import Flask
from flask import request, jsonify
from flask_cors import CORS
import os
import db

default_params = {
    'user': 'root',
    'password': 'notes',
    'host': 'localhost',
    'database': 'db'
}

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello():
    return "Hello"


@app.route('/check_init')
def check_init():
    initialized = db.is_initialized(default_params)
    return {'data': initialized}


@app.route('/categories/')
def get_categories():
    query = db.select("*", 'category')
    result = db.run_query(query, default_params, select=True)
    return {'data': result}


@app.route('/notes/')
def get_notes():
    query = db.select("*", 'note', 'deleted = 0')
    result = db.run_query(query, default_params, select=True)
    return {'data': result}


@app.route('/notes/<cat_id>')
def get_notes_by_cat(cat_id):
    query = db.select("*", 'note', 'deleted = 0 and cat_id = ' + cat_id)
    result = db.run_query(query, default_params, select=True)
    return {'data': result}


@app.route('/note/<note_id>')
def get_note(note_id):
    query = db.select("*", 'note', 'deleted = 0 and id = ' + note_id)
    result = db.run_query(query, default_params, select=True)
    return {'data': result}


@app.route('/insert/note', methods=['POST'])
def insert_note():
    r = request.form

    title = "'" + r['title'] + "'"
    data = "'" + r['data'] + "'"
    cat_id = "'" + r['cat_id'] + "'"
    deleted = "'" + '0' + "'"

    columns = '(title, data, cat_id, deleted)'

    data = ','.join([title, data, cat_id, deleted])
    query = db.insert(data, 'note', columns)
    db.run_query(query, default_params)
    return ''


@app.route('/insert/category', methods=['POST'])
def insert_category():
    r = request.form

    cat_name = "'" + r['cat_name'] + "'"

    columns = '(name)'

    data = cat_name
    query = db.insert(data, 'category', columns)
    db.run_query(query, default_params)
    return ''


@app.route('/delete/<note_id>', methods=['POST'])
def delete_note(note_id):
    query = db.update('note', 'deleted', 1, 'id = ' + note_id)
    db.run_query(query, default_params)
    return ''


@app.route('/initialize', methods=['POST'])
def initialize_db():
    db.initialize_db(default_params)
    return ''


if __name__ == "__main__":
    app.run(host='0.0.0.0')
