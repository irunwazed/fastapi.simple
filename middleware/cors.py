from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

origins = [
  "http://localhost:3000",
  "http://127.0.0.1:3000",
]

def cors_middleware(app: FastAPI):
  app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
  )