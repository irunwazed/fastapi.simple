from fastapi import APIRouter, Request, Depends  # type: ignore
from dto.response import *
from library.depends import  get_current_user, get_db
from api import beranda
from typing import Annotated

router = APIRouter(
  prefix="/beranda",
  tags=["beranda"],
  dependencies=[Depends(get_current_user), Depends(get_db)]
)

@router.get('', responses={200: {"model": DataRespon}})
def home(req:Request):
  return beranda.beranda(req)