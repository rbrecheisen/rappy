from flask import Flask, Blueprint
from flask_restful import Api
from rappy.rest.api import IndexResource
from rappy.rest.api import Tag2DcmResource
from rappy.rest.api import ExtractMasksResource

app = Flask(__name__)
blueprint = Blueprint('rappy', __name__)
api = Api(blueprint)

api.add_resource(IndexResource, IndexResource.URI)
api.add_resource(Tag2DcmResource, Tag2DcmResource.URI)
api.add_resource(ExtractMasksResource, ExtractMasksResource.URI)

app.register_blueprint(blueprint)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
