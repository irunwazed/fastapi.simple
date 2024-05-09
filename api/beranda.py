
from fastapi.responses import JSONResponse # type: ignore
from dataclasses import asdict
from model.user import User

def beranda(req):
  db = req.state.db
  user = db.query(User).filter(User.username=="tes").first()
  print("req.state")
  print(req.state.user['username'])
  if not user:
    print("NO DATA")
  return {"masuk":"PAK EKO"}