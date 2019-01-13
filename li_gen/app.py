from datetime import datetime

from flask import Flask, render_template_string, request
from peewee import CharField, Model, SqliteDatabase, TextField

app = Flask(__name__)
db = SqliteDatabase('licenses.db')


class License(Model):
    name = CharField()
    text = TextField()

    class Meta:
        database = db


@app.route('/')
def index():
    return 'Hello world'


@app.route('/license')
def license():
    return render_template_string(
        f'<pre>{License.get(License.name == request.args.get("license")).text}</pre>',
        **{'year': datetime.now().year, **request.args}
    )


@app.errorhandler(404)
def not_found(error):
    return 'Not found'


@app.errorhandler(500)
def server_error(error):
    return 'Something went wrong'


if __name__ == '__main__':
    app.run(debug=True)
