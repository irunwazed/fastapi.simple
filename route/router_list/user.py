from fastapi import APIRouter, Request, Depends, Form  # type: ignore
from dto.response import *
from library.depends import  get_current_user, get_db
from api import user
from typing import Annotated
from enum import Enum

router = APIRouter(
  prefix="/user",
  tags=["user"],
  dependencies=[Depends(get_current_user), Depends(get_db)]
)

class dropdownChoices(str, Enum):
  admin = "Admin"
  user = "User"

def form_create_user(name: Annotated[str, Form()], username: Annotated[str, Form()], password: Annotated[str, Form()], role: dropdownChoices = Form(dropdownChoices.user)):
  return {"name": name, "username": username, "password": password, "role": role}

@router.post('', responses={200: {"model": DataRespon}})
def create_user(req:Request, form: Annotated[dict, Depends(form_create_user)]):
  return user.create(req, form)

@router.get('', responses={200: {"model": DataRespon}})
def get_all_users(req:Request):
  return user.get_all(req)

@router.get('/{id}', responses={200: {"model": DataRespon}})
def get_one_user(req:Request, id):
  return user.get_one(req, id)

@router.put('/{id}', responses={200: {"model": DataRespon}})
def update_user(req:Request, id, form: Annotated[dict, Depends(form_create_user)]):
  return user.update(req, id, form)

@router.delete('/{id}', responses={200: {"model": Response}})
def delete_user(req:Request, id):
  return user.delete(req, id)