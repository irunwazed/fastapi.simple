
from dataclasses import dataclass
from .auth import Token

@dataclass
class Response:
  status: bool
  message: str


@dataclass
class DataRespon:
  status: bool
  message: str
  data: dict



@dataclass
class NotFoundResponse:
  status: bool
  message: str


@dataclass
class NotAuthResponse:
  status: bool
  message: str


@dataclass
class LoginFailureResponse:
  status: bool
  message: str


@dataclass
class LoginSuccessResponse:
  status: bool
  message: str
  data: Token

