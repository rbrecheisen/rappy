import json
from logging.config import dictConfig
from flask import Flask, Blueprint, make_response
from flask_restful import Api
from rappy.rest.api import Tag2DcmResourceList, Tag2DcmResource

# Setup logging
dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'root': {
        'level': 'INFO',
    }
})

# Initialize app and api
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/tmp/rappy'
blueprint = Blueprint('rappy', __name__)
api = Api(blueprint)

# Setup API
api.add_resource(Tag2DcmResourceList, '/tag2dcm')
api.add_resource(Tag2DcmResource, '/tag2dcm/<string:file_id>')

app.register_blueprint(blueprint)


@api.representation('application/json')
def output_json(data, code, headers=None):
    response = make_response(json.dumps(data), code)
    response.headers.extend(headers or {})
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
