# import dependencies
# import os
# from dotenv import load_dotenv
from flask import Flask, jsonify,render_template, current_app
import psycopg2
from bird import Bird
from settings import DATABASE, USER

# from .settings import DATABASE, USER


app = Flask(__name__, static_folder='../data/bird-training-images/', template_folder='../templates/')

# without settings.py. direct to .env
# load_dotenv()
# DATABASE = os.getenv('DATABASE')
# USER = os.getenv('USER')

# app.config.from_mapping(
#     DATABASE = os.getenv('DATABASE'),
#     USER = os.getenv('USER')
# )

# with settings.py:
app.config['DATABASE'] = DATABASE
app.config['USER'] = USER



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

# '/api/birds/<id>' path is a dedicated route to serve JSON for the API
@app.route('/birds/api/<id>')
def bird_api(id):
    try:
        # Connect to the database
        conn = psycopg2.connect(database=app.config['DATABASE'], user=app.config['USER'])
        cursor = conn.cursor()
        # Execute the query to fetch bird data
        cursor.execute("SELECT * FROM birds WHERE id = %s LIMIT 1;", (id, ))
        bird_data = cursor.fetchone()
        # If bird data is found, return it as JSON
        if bird_data:
            bird = Bird(bird_data)
            bird_dict = bird.__dict__
            return jsonify(bird_dict)
        else:
            # If not found, return an error message
            return jsonify({"error": "Bird not found"}), 404
    except Exception as e:
        # Log the exception
        current_app.logger.error(f"An error occurred: {e}")
        # Return a generic error message
        return jsonify({"error": "An unexpected error occurred"}), 500

# '/birds/image/<id>' route is dedicated to serving HTML page that displays the bird image
@app.route('/birds/image/<id>')
def bird_image(id):
    # Connect to the database
    conn = psycopg2.connect(database=app.config['DATABASE'], user=app.config['USER'])
    cursor = conn.cursor()
    # Execute the query to fetch bird data
    cursor.execute("SELECT * FROM birds WHERE id = %s LIMIT 1;", (id,))
    bird_data = cursor.fetchone()
    # If bird data is found, render the template with the image URL
    if bird_data:
        bird = Bird(bird_data)
        bird_image = bird.image_url()
        return render_template('bird_image.html', image_url=bird_image)
    else:
        # If not found, return an error message
        return jsonify({"error": "Bird not found"}), 404

app.run(debug=True)

