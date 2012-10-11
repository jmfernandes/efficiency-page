import os
import json
from flask import Flask

app = Flask(__name__)

@app.route('/physics/standardgravity')
def hello():
    dict = {'value': 9.80665, 'units': 'meters/(seconds^2)', 'citation': 'http://en.wikipedia.org/wiki/Standard_gravity','name': 'standard gravity'};
    data = json.dumps(dict)
    return data

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)