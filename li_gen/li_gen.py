from datetime import datetime

from quart import Quart, request, render_template_string

from models import License


app = Quart(__name__)


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
    return 'Not found, weirdo'

@app.errorhandler(500)
def server_error(error):
    return 'Something went wrong'

app.run()
