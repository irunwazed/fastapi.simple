from fastapi.responses import JSONResponse # type: ignore
from dataclasses import asdict
from model.user import User
from library.utils import get_password_hash
from fastapi.encoders import jsonable_encoder
from dto.response import Response


def create(req, form):
  db = req.state.db
  create_user = User(name=form["name"], username=form["username"], password=get_password_hash(form["password"]), role=form["role"])
  db.add(create_user)
  db.commit()
  
  return JSONResponse(status_code=201, content={
    "status": True,
    "message": "Berhasil Input Data",
  })
  
def get_all(req):
  db = req.state.db
  users = db.query(User).limit(10).offset(0).all()
  return JSONResponse(status_code=200, content={
    "status": True,
    "message": "Berhasil Get Data",
    "data": jsonable_encoder(users)
  })

def get_one(req, id):
  db = req.state.db
  user = db.query(User).filter_by(id=id).one()
  return JSONResponse(status_code=200, content={
    "status": True,
    "message": "Berhasil Get Data",
    "data": jsonable_encoder(user)
  })

def update(req, id, form):
  db = req.state.db
  update_query = {User.name: form["name"], User.username: form["username"], User.password: get_password_hash(form["password"]), User.role: form["role"]}
  db.query(User).filter_by(id=id).update(update_query)
  db.commit()
  user = db.query(User).filter_by(id=id).one()
  return JSONResponse(status_code=200, content={
    "status": True,
    "message": "Berhasil Ubah Data",
    "data": jsonable_encoder(user)
  })

def delete(req, id):
  db = req.state.db
  post = db.query(User).filter_by(id=id).all()
  if not post:
      return Response(False, "Data tidak ditemukan")
  db.query(User).filter_by(id=id).delete()
  db.commit()
  return JSONResponse(status_code=200, content={
    "status": True,
    "message": "Berhasil Hapus Data",
  })