from sqlalchemy import create_engine # type: ignore
from sqlalchemy.orm import sessionmaker # type: ignore
from dotenv import load_dotenv # type: ignore
from sqlalchemy.sql import text  # type: ignore
load_dotenv()
import os


DB_URL = DB_URL = os.getenv("DB_URL")
engine = create_engine(DB_URL,echo=True)
SessionLocal = sessionmaker(autocommit=False,autoflush=False, bind=engine)


def get_db():
  db = SessionLocal()
  try : 
    yield db
  finally:
    db.close()


def get_data(query:str, data={}):
  result = None
  db = SessionLocal()
  try:
    sql = text(query)
    result = db.execute(sql, data)
  except Exception as e:
    print(e)
  finally:
    db.close()
  return result


def get_data_first(query:str, data={}):
  result = None
  db = SessionLocal()
  try:
    sql = text(query)
    temp = db.execute(sql, data)
    for row in temp:
      result = row
      break
  except Exception as e:
    print(e)
  finally:
    db.close()
  return result




