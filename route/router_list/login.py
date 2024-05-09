from typing import Annotated
from fastapi import APIRouter, Depends, Request # type: ignore
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm # type: ignore
from library.depends import db_dependency
from dto.auth import Token
from dto.response import Response, LoginSuccessResponse
from dto.request import LoginRequest
from library.depends import get_db
from api import login

router = APIRouter(
  prefix="/login",
  tags=["login"],
  dependencies=[Depends(get_db)]
)

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="login/token")

@router.post("", responses={200: {"model": LoginSuccessResponse}, 401: {"model": Response}})
async def login_with_username_password(req: Request, form: LoginRequest):
  return login.check_login_from(req.state.db, form)

@router.post("/token", responses={200: {"model": Token}, 401: {"model": Response}}, include_in_schema=False)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db:db_dependency):
  return login.check_login(db, form_data)
