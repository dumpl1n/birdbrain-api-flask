# import dependencies
import os
from flask import Flask, jsonify
import psycopg2
from bird import Bird

app = Flask(__name__)

#use the `app.config.from_mapping` method to set these variables on our flask application
app.config.from_mapping(
    DATABASE = os.getenv('DATABASE'),
    USER = os.getenv('USER')
)

@app.route('/birds')
def venues():
    conn = psycopg2.connect(database = 'DATABASE', user = 'USER')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM birds;')
    venues = cursor.fetchall()
    bird_objs = Bird(bird).__dict__ for bird in birds]
    return jsonify(bird_objs)

@app.route('/birds/<id>')
def show_venue(id):
    conn = psycopg2.connect(database = 'DATABASE', user = 'USER')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM venues WHERE id = %s LIMIT 1;", id)
    bird_inst = cursor.fetchone()
    return jsonify(Bird(bird_inst).__dict__)

app.run(debug = True)

