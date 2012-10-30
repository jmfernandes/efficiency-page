import os
import flask, flask.views

app = flask.Flask(__name__)

class View(flask.views.MethodView):
	def get(self):
		return flask.render_template('efficiency.html')

app.add_url_rule('/', view_func=View.as_view('main'), methods=['get'])

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)