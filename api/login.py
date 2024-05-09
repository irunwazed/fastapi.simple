from fastapi.responses import JSONResponse # type: ignore
from dataclasses import asdict
from dto.response import LoginSuccessResponse
from dto.auth import Token
from library.utils import  verify_password, create_token


from model.user import User

def check_login_from(db, form):
  user = check_user(db, form.username, form.password)
  if not user:
    return JSONResponse(status_code=401, content={"status": False, "message": "Username atau Password salah"})
  token = get_token(user)
  response = LoginSuccessResponse(True, "Berhasil Login", Token(token, "Bearer"))
  return JSONResponse(status_code=200, content=asdict(response))

def check_login(db, form):
  user = check_user(db, form.username, form.password)
  if not user:
    return JSONResponse(status_code=401, content={"status": False, "message": "Username atau Password salah"})
  token = get_token(user)
  response = Token(token, "Bearer") #LoginSuccessResponse(True, "Berhasil Login", Token(token, "Bearer"))
  return JSONResponse(status_code=200, content=asdict(response))

def check_user(db, username: str, password: str):
  try:
    user = db.query(User).filter(User.username==username).first()
    if not user:
      return False
    if not verify_password(password, user.password):
      return False
    return user
  except Exception as e:
    print("ERROR : ", e)
    return False
  
def get_token(user):
  return create_token(
    data={
      "sub": user.username
    }
  )
