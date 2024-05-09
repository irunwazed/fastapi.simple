
from typing import Annotated
from fastapi import Depends, HTTPException, Request
from starlette import status # type: ignore
from db.db import SessionLocal
from fastapi.security import OAuth2PasswordBearer
from library.utils import get_payload_token

from sqlalchemy.orm import Session # type: ignore
from core.response import page_not_auth


oauth2_bearer = OAuth2PasswordBearer(tokenUrl="login/token")

def get_bearer():
  return "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTcxNTIxNTQ0M30.fvgdXmJnCvLll54rEJ3F-Uh0ckvWmq_bJw7Ixe26cAM"

def get_db(req: Request):
  db = SessionLocal()
  req.state.db = db
  try : 
    yield db
  finally:
    db.close()

  
def get_current_user(req:Request, token: Annotated[str, Depends(oauth2_bearer)]):
  try:
    payload = get_payload_token(token)
    username:str = payload.get("sub")
    if username is None:
      return page_not_auth() # HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token")
    req.state.user = {"username": username}
  except Exception as e:
    print("ERROR GET USER TOKEN : ", e)

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]