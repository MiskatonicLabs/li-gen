from datetime import datetime
from functools import total_ordering

from flask import Flask, render_template, render_template_string, request
from peewee import CharField, Model, PostgresqlDatabase, TextField

app = Flask(__name__)
db = PostgresqlDatabase('li-gen')


@total_ordering
class License(Model):
    name = CharField()
    text = TextField()

    class Meta:
        database = db

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.name < other.name

    def __str__(self):
        return self.name


@app.route('/')
def index():
    return render_template('index.html', licenses=sorted(License.select()))


@app.route('/license')
def license():
    license_text = License.get(License.name == request.args.get('license')).text

    if not request.args.get('raw', '').lower() == 'true':
        return render_template_string(f'<pre>{license_text}</pre>', **{'year': datetime.now().year, **request.args})

    return render_template_string(license_text, **{'year': datetime.now().year, **request.args})


@app.errorhandler(404)
def not_found(error):
    return 'Not found'


@app.errorhandler(500)
def server_error(error):
    return 'Something went wrong'


if __name__ == '__main__':
    app.run(debug=True)
