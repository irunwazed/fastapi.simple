from fastapi import FastAPI # type: ignore
from starlette.exceptions import HTTPException as StarletteHTTPException  # type: ignore
from core.response import page_not_found, page_not_auth, page_error


def page_handler(app: FastAPI):
  @app.exception_handler(404)
  async def not_found_page(request, exc):
    return page_not_found()

  @app.exception_handler(401)
  async def not_found_page(request, exc):
    return page_not_auth()

  @app.exception_handler(500)
  async def not_found_page(request, exc):
    return page_error(exc)

  @app.exception_handler(StarletteHTTPException)
  async def http_exception_handler(request, exc):
    return page_not_found()