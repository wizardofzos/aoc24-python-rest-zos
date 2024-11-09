from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs
from flask_restful import Resource
from flask import abort

from subprocess import Popen, PIPE
import uuid
import os
import datetime

from .fileupload import FileSchema

#  Restful way of creating APIs through Flask Restful
class PYTHON(MethodResource, Resource):
    @doc(description='This is an example PYTHON solution. Also just counts the number of lines in the input file', tags=['PYTHON'],
    responses={
        '200': {'description': 'Everything is ok!'},
    }
    )
    
    @use_kwargs(FileSchema, location='files')
    def post(self, puzzle):
        # stick the file somewhere
        infile = f"/tmp/{uuid.uuid4()}"
        puzzle.save(infile)  # will go be iso8859-1 
        from collections import deque as de
        start = datetime.datetime.now()
        solution = 0
        x = open(infile,"r").readlines()
        for i in range(len(x)):
            solution += 1
        
        stop = datetime.datetime.now()

        
        os.remove(infile)  

        return {'solution': solution, 'duration': f"{stop-start}"}