from datetime import datetime

from flask import Flask, g, render_template, render_template_string, request

from .api.api import api
from .config import Config
from .models import License

app = Flask(__name__)
app.register_blueprint(api)

app.config['SECRET_KEY'] = Config.SECRET_KEY


@app.before_request
def before_request():
    g.db = Config.db
    g.db.connect()


@app.after_request
def after_request(response):
    g.db.close()
    return response


@app.errorhandler(404)
def not_found(error):
    return 'Not found'


@app.errorhandler(500)
def server_error(error):
    return 'Something went wrong'


@app.route('/')
def index():
    return render_template('index.html', licenses=sorted(License.select()))


@app.route('/license')
def license():
    license_text = License.get(License.name == request.args.get('license')).text

    if not request.args.get('raw', '').lower() == 'true':
        return render_template_string(f'<pre>{license_text}</pre>', **{'year': datetime.now().year, **request.args})

    return render_template_string(license_text, **{'year': datetime.now().year, **request.args})


if __name__ == '__main__':
    app.run(debug=True)
