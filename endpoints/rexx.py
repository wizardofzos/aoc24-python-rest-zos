from marshmallow import Schema, fields
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs
from flask_restful import Resource
from flask import abort

from subprocess import Popen, PIPE

import uuid
import os
import datetime
import sys

from .fileupload import FileSchema
sys.path.append('../constants')



from constants import REXX_PATH 

#  Restful way of creating APIs through Flask Restful
class REXX(MethodResource, Resource):
    
    @doc(description="A placeholder for running rexx-solutions.<br />This" + 
    "example rexx just returns the amount of lines from the input." 
    , tags=['REXX'],
    responses={
        '200': {'description': 'Everything is ok!'},
    }
    )
    @use_kwargs(FileSchema, location='files')
    def post(self, puzzle):
        # stick the file somewhere
        infile = f"/tmp/{uuid.uuid4()}"
        gofile = f"/tmp/{uuid.uuid4()}"
        puzzle.save(infile)  # will go be iso8859-1
        os.system(f"iconv -f iso8859-1 -t ibm-1047 {infile} > {gofile}")
        os.system(f"chtag -tc ibm-1047 {gofile}")
        # Run the REXX
        start   = datetime.datetime.now()
        process = Popen([f'{REXX_PATH}/example.rex',gofile], stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        
        stop = datetime.datetime.now()
        duration = stop - start
        print(stdout.decode('utf-8'))
        print(stderr.decode('utf-8'))
        parts = stdout.decode('utf-8').split('=')
        print(parts)
        os.remove(infile)
        os.remove(gofile)
        result = {}
        result['duration'] = f"{duration}"

        if parts[0] == "solution":
            result['solution'] = int(parts[1].strip())
        else:
            result['solution': '*FAILED*']
        return result



