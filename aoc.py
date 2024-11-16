from flask import Flask
from flask_restful import Resource, Api
from apispec import APISpec
from marshmallow import Schema, fields
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs

app = Flask(__name__)  
api = Api(app)  


app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Advent of Code 2024',
        version='v1',
        info={'description': 'My <a href="https://adventofcode.com">Advent of Code 2024</a> solutions.' +
        '<br />Github Repo: <a href="https://github.com/wizardofzos/aoc24-python-rest-zos">github.com/wizardofzos/aoc24-python-rest-zos</a>'+
        '<br /><b>Warning</b>:All [POST] endpoints assume a puzzle input with "Windows Line Ends "' +
        '(meaning a single 0x0d).'},
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/swagger/',       
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'  
})
docs = FlaskApiSpec(app)

class ResponseSchema(Schema):
    '''
    All solutions should post results in the field solution :)
    '''    
    solution = fields.Str(default='The answer')

# our examples
from endpoints import REXX, PYTHON, COBOL
api.add_resource(REXX, '/rexx')
docs.register(REXX)
api.add_resource(PYTHON, '/python')
docs.register(PYTHON)
api.add_resource(COBOL, '/cobol')
docs.register(COBOL)

from endpoints import *
# Add the solutions per day per part...
# api.add_resource(REXXD01P1, '/d01p1-rexx')
# docs.register(REXXD01P1)
# api.add_resource(PYTHOND01P1, '/d01p1-pyton')
# docs.register(PYTHOND01P1)

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 12345))
    app.run(debug=True, host='0.0.0.0', port=port)