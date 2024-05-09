from dataclasses import asdict, dataclass, make_dataclass
from jose import JWTError, jwt
from datetime import datetime, timezone, timedelta
from passlib.context import CryptContext
from config.config import  ALGORITHM, SECRET_KEY, ACCESS_TOKEN_EXPIRE_MINUTES

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def ResponData( MyClass):
  return make_dataclass("ResponUser", [('message', str), ("status", bool), ("data", MyClass)])

def verify_password( plain_password, hashed_password):
  return pwd_context.verify(plain_password, hashed_password)

def get_password_hash( password):
  return pwd_context.hash(password)

def create_token( data: dict):
  to_encode = data.copy()
  expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
  expire = datetime.now(timezone.utc) + expires_delta
  to_encode.update({"exp": expire})
  encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
  return encoded_jwt

def create_access_token( data: dict, expires_delta: timedelta | None = None):
  to_encode = data.copy()
  if expires_delta:
    expire = datetime.now(timezone.utc) + expires_delta
  else:
    expire = datetime.now(timezone.utc) + timedelta(minutes=15)
  to_encode.update({"exp": expire})
  encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
  return encoded_jwt

def get_payload_token( token):
  return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
