from fastapi import APIRouter, Request # type: ignore
# from dataclasses import make_dataclass

class Router:
  app: APIRouter
  req: Request

  def __init__(self, prefix: str) -> None:
    super().__init__()
    self.app = APIRouter(prefix=prefix)

  def GET(self, path:str, func, request=None, responses = None):
    @self.app.get(path, responses=responses)
    def get(item:int=1):
      print(item)
      return func(item)
  
  def POST(self, path:str, func, request=None, responses = None):
    @self.app.post(path, responses=responses)
    def post(req:Request, form:request):
      return func(req, form)
    
  def router(self):
    return self.app