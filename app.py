import os
from flask import Flask, render_template, json

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.route('/')
def index():
    return render_template('efficiency.html')

"""Web Pages"""

@app.route('/biological/photosynthesis_crops', endpoint='/biological/photosynthesis_crops')
def index():
    json_file = open('templates/json/biological/photosynthesis_crops.json')
    data = json.load(json_file)
    json_file.close()
    return render_template('webpage.html',data=data)

@app.route('/biological/photosynthesis_sugarcane', endpoint='/biological/photosynthesis_sugarcane')
def index():
    json_file = open('templates/json/biological/photosynthesis_sugarcane.json')
    data = json.load(json_file)
    json_file.close()
    return render_template('webpage.html',data=data)

"""JSON Pages"""

@app.route('/biological/photosynthesis_crops_json', endpoint='/biological/photosynthesis_crops_json')
def index():
    return render_template('json/biological/photosynthesis_crops.json')

@app.route('/biological/photosynthesis_sugarcane_json', endpoint='/biological/photosynthesis_sugarcane_json')
def index():
    return render_template('json/biological/photosynthesis_sugarcane.json')


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)