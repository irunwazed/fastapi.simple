
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Boolean, Column, Table, ForeignKey, Integer, String # type: ignore

Base = declarative_base()

class User(Base):
  __tablename__ = "users"
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String(255))
  username = Column(String(255), unique=True, index=True)
  password = Column(String(255))
  role = Column(String(50))
  is_active = Column(Boolean,default=False)