from datetime import datetime
from dataclasses import dataclass

@dataclass
class LoginUser:
    username: str
    password: str
    exp: datetime
