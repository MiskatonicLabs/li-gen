from datetime import datetime

from peewee import CharField, Model, SqliteDatabase, TextField
from quart import Quart, render_template_string, request

app = Quart(__name__)
db = SqliteDatabase('licenses.db')


class License(Model):
    name = CharField()
    text = TextField()

    class Meta:
        database = db


@app.route('/')
async def index():
    return 'Hello world'


@app.route('/license')
async def license():
    return await render_template_string(
        f'<pre>{License.get(License.name == request.args.get("license")).text}</pre>',
        **{'year': datetime.now().year, **request.args}
    )


@app.errorhandler(404)
def not_found(error):
    return 'Not found'


@app.errorhandler(500)
def server_error(error):
    return 'Something went wrong'


app.run()
