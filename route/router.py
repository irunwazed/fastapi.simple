from fastapi import FastAPI # type: ignore
from .router_list import login,  beranda, user

app = FastAPI(title="Pengolahan Nilai", description="Sistem Pengolahan Nilai SSCASN", version="0.1.0")

app.include_router(login.router)
app.include_router(beranda.router)
app.include_router(user.router)
