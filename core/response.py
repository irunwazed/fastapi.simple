
from fastapi.responses import JSONResponse # type: ignore
from dataclasses import asdict
from dto.response import NotAuthResponse, NotFoundResponse

import os
NODE_ENV = os.getenv("NODE_ENV")

def page_not_found():
  response = NotFoundResponse(message="Page Not Found", status=False)
  return JSONResponse(status_code=404, content=asdict(response))

def page_not_auth():
  response = NotAuthResponse(message="Page Not Authorization", status=False)
  return JSONResponse(status_code=401, content=asdict(response))

def page_error(exc):
  if NODE_ENV == 'development':
    response = NotAuthResponse(message="ERROR : "+str(exc), status=False)
  else:
    response = NotAuthResponse(message="ERROR!!!", status=False)
  return JSONResponse(status_code=500, content=asdict(response))