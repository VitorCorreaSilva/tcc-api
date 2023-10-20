from flask import Flask
from flask_restx import Api
from werkzeug.datastructures import FileStorage

app = Flask(__name__)
app.config['SECRET_KEY'] = b'\x11R\xdd?G\x02|\xdfD\xc5\xcb\xad\xcc\xa2\xf0\xca\xdes&\xd0\x05\xc2\xbfF'
app.config['ERROR_404_HELP'] = False

api = Api(app)
health_namespace= api.namespace('health', "Verifica a saúde do serviço.")
load_namespace = api.namespace('load', description='Conjunto de funções para carregar os arquivos')
upload_parser = api.parser()
upload_parser.add_argument('file', location='files',type=FileStorage, required=True)

from api import routes