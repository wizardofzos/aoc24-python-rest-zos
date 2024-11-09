from marshmallow import Schema, fields
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs
from flask_restful import Resource
from flask import abort

import uuid
import os

from subprocess import Popen, PIPE
from .fileupload import COBOLFileSchema

#  Restful way of creating APIs through Flask Restful
class COBOL(MethodResource, Resource):
    @doc(description='An example COBOL-solution endpoint.\nVery very trial and not done yet :)\nMake sure the cobol source has LF line endings...', tags=['COBOL'],
    responses={
        '200': {'description': 'Everything is ok!'},
    }
    )
    @use_kwargs(COBOLFileSchema, location='files')
    def post(self, cobolsource, puzzle=None):
        # COMPILE THE COBOL
        infile = f"/tmp/{uuid.uuid4()}"
        cobsrc = f"/tmp/{uuid.uuid4()}.cbl"
        gofile = f"/tmp/{uuid.uuid4()}"
        cobolsource.save(infile)  # will be iso8859-1
        os.system(f"iconv -f iso8859-1 -t ibm-1047 {infile} > {cobsrc}") # make ebcdic
        os.system(f"chtag -tc ibm-1047 {cobsrc}")  # tag it and bag it
        process = Popen(['cob2', cobsrc], stdout=PIPE, stderr=PIPE) # compile it :)
        stdout, stderr = process.communicate()
        exit_code = process.wait()
        errlines = stderr.decode('cp1047').split('\n')
        print(stdout.decode('cp1047'))
        print(errlines)
        print(exit_code)
        if exit_code < 4:
            process = Popen(['./a.out'], stdout=PIPE, stderr=PIPE) # run it :)
            progout, progerr = process.communicate()
            result = progout.decode('utf-8')
        else:
            result = "Compiler Errors"
        return {'result':result,'compiler-out':errlines}
