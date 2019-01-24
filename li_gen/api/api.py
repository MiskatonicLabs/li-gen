from flask import Blueprint, request
from flask import jsonify


from li_gen.models import License


api = Blueprint('api', __name__, url_prefix='/api/v1.0')


@api.route('/licenses', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return jsonify({'licenses': [license.name for license in License.select()]})
