from datetime import datetime
from dataclasses import dataclass

@dataclass
class LoginUser:
    user_id: int
    username: str
    exp: datetime
