import flask, flask.views
import os
app = flask.Flask(__name__)
# Don't do this!
app.secret_key = "bacon"

class View(flask.views.MethodView):
    def get(self):
        return flask.render_template('efficiency.html')
    def post(self):
        result = eval(flask.request.form['expression'])
        flask.flash(result)
        return self.get()

app.add_url_rule('/', view_func=View.as_view('main'), methods=['GET', 'POST'])

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)