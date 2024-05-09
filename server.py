
from route.router import app
from middleware import cors, page


cors.cors_middleware(app=app)
page.page_handler(app)