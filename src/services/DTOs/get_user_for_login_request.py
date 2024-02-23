from dataclasses import dataclass

@dataclass
class GetUserForLogin:
    username: str
    password: str
