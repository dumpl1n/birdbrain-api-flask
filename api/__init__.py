# import dependencies
import os
from flask import Flask, jsonify, request, render_template
import psycopg2
from bird import Bird

app = Flask(__name__, static_folder='../data/bird-training-images/', template_folder='../templates/')
# app = Flask(__name__, static_folder='data/', template_folder=os.path.join(basedir, 'templates'))
#use the `app.config.from_mapping` method to set these variables on our flask application
app.config.from_mapping(
    DATABASE = os.getenv('DATABASE'),
    USER = os.getenv('USER')
)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/birds')
def birds():
    conn = psycopg2.connect(database=app.config['DATABASE'], user=app.config['USER'])
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM birds;')
    birds = cursor.fetchall()
    bird_objs = [Bird(bird).__dict__ for bird in birds]
    return jsonify(bird_objs)

@app.route('/birds/<id>')
def show_bird(id):
    conn = psycopg2.connect(database=app.config['DATABASE'], user=app.config['USER'])
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM birds WHERE id = %s LIMIT 1;", (id,))
    bird_data = cursor.fetchone()
    if bird_data:
        bird = Bird(bird_data)
        # bird_dict = bird.__dict__
        # bird_dict['image_url'] = bird.image_url()
        bird_image = bird.image_url()
        return render_template('bird_image.html', image_url=bird_image) # jsonify(bird_dict)
    else:
        return jsonify({"error": "Bird not found"}), 404
    # return jsonify(Bird(bird_data).__dict__)


app.run(debug = True)

