from api import arquivo

from api import load_namespace, health_namespace, upload_parser
from flask_restx import Resource

@health_namespace.route("/")
class Saude(Resource):
    def get(self):
        return {
            "online": True
        }


@load_namespace.route("/arquivo/upload")
@load_namespace.expect(upload_parser)
class Arquivo(Resource):
    def post(self):
        args = upload_parser.parse_args()
        uploaded_file = args['file']
        return arquivo.upload(uploaded_file)