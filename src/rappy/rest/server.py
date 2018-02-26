from logging.config import dictConfig
from flask import Flask, Blueprint
from flask_restful import Api
from rappy.rest.api import IndexResource
from rappy.rest.api import Tag2DcmResource
from rappy.rest.api import ExtractMasksResource

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
blueprint = Blueprint('rappy', __name__)
api = Api(blueprint)

# Setup API
api.add_resource(IndexResource, IndexResource.URI)
api.add_resource(Tag2DcmResource, Tag2DcmResource.URI)
api.add_resource(ExtractMasksResource, ExtractMasksResource.URI)
# api.add_resource(ExtractPyRadiomicsFeaturesResource, ExtractPyRadiomicsFeaturesResource.URI)
app.register_blueprint(blueprint)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
