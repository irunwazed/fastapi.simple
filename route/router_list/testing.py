# import api.login
# from fastapi import FastAPI, Request, APIRouter # type: ignore

# from core.router import Router
# import api
# from dto.respon import *
# from dto.request import *


# def login_route(app: FastAPI, prefix:str):
#   route = Router(prefix=prefix)

#   route.GET("/tes", api.login.show_login)
#   route.GET("/tes2", api.login.show_login_param, request=RequestLogin, responses={201: {"model": ResponData}} )
#   route.POST("/login", api.login.login, request=RequestLogin, responses={201: {"model": ResponData}} )

#   app.include_router(route.router())

# import api.login
# from fastapi import APIRouter, Request  # type: ignore
# import api
# from dto.respon import *
# from dto.request import RequestLogin
# from fastapi.responses import JSONResponse # type: ignore
# from dataclasses import asdict

# module="login"
# router = APIRouter(prefix="/"+module)

# @router.post('', responses={200: {"model": ResponData}}, tags=[module])
# def post(req: Request, form:RequestLogin):
#   try:
#     return api.login.login(req, form)
#   except Exception as e:
#     response = Respon(False, "Server Error!")
#     return JSONResponse(status_code=500, content=asdict(response)) 

# @router.post('/check', responses={200: {"model": ResponData}}, tags=[module])
# def post(req: Request, form:RequestLogin):
#   return api.login.check(req, form)
