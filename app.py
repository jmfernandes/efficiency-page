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

@app.route('/mechanical/fluorescent', endpoint='/mechanical/fluorescent')
def index():
    json_file = open('templates/json/mechanical/fluorescent.json')
    data = json.load(json_file)
    json_file.close()
    return render_template('webpage.html',data=data)

@app.route('/mechanical/led', endpoint='/mechanical/led')
def index():
    json_file = open('templates/json/mechanical/led.json')
    data = json.load(json_file)
    json_file.close()
    return render_template('webpage.html',data=data)

@app.route('/mechanical/metal_halide', endpoint='/mechanical/metal_halide')
def index():
    json_file = open('templates/json/mechanical/metal_halide.json')
    data = json.load(json_file)
    json_file.close()
    return render_template('webpage.html',data=data)

@app.route('/mechanical/tungsten_bulb', endpoint='/mechanical/tungsten_bulb')
def index():
    json_file = open('templates/json/mechanical/tungsten_bulb.json')
    data = json.load(json_file)
    json_file.close()
    return render_template('webpage.html',data=data)

@app.route('/chemical/krebs_cycle', endpoint='/chemical/krebs_cycle')
def index():
    json_file = open('templates/json/chemical/krebs_cycle.json')
    data = json.load(json_file)
    json_file.close()
    return render_template('webpage.html',data=data)

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

@app.route('/natural/luminosity_sun', endpoint='/natural/luminosity_sun')
def index():
    json_file = open('templates/json/natural/luminosity_sun.json')
    data = json.load(json_file)
    json_file.close()
    return render_template('webpage.html',data=data)

"""JSON Pages"""

@app.route('/mechanical/fluorescent_json', endpoint='/mechanical/fluorescent_json')
def index():
    return render_template('json/mechanical/fluorescent.json')

@app.route('/mechanical/led_json', endpoint='/mechanical/led_json')
def index():
    return render_template('json/mechanical/led.json')

@app.route('/mechanical/metal_halide_json', endpoint='/mechanical/metal_halide_json')
def index():
    return render_template('json/mechanical/metal_halide.json')

@app.route('/mechanical/tungsten_bulb_json', endpoint='/mechanical/tungsten_bulb_json')
def index():
    return render_template('json/mechanical/tungsten_bulb.json')

@app.route('/chemical/krebs_cycle_json', endpoint='/chemical/krebs_cycle_json')
def index():
    return render_template('json/chemical/krebs_cycle.json')

@app.route('/biological/photosynthesis_crops_json', endpoint='/biological/photosynthesis_crops_json')
def index():
    return render_template('json/biological/photosynthesis_crops.json')

@app.route('/biological/photosynthesis_sugarcane_json', endpoint='/biological/photosynthesis_sugarcane_json')
def index():
    return render_template('json/biological/photosynthesis_sugarcane.json')

@app.route('/natural/luminosity_sun_json', endpoint='/natural/luminosity_sun_json')
def index():
    return render_template('json/natural/luminosity_sun.json')


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)