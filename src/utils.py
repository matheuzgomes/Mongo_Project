import os
from datetime import datetime, timedelta
from typing import Dict, Any
from fastapi import Security, HTTPException, status, Depends
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer
from pydantic import ValidationError
from dataclasses import dataclass
from passlib.context import CryptContext
from .services.DTOs import LoginUser

ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 # 7 days
ALGORITHM = "HS256"
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
JWT_REFRESH_SECRET_KEY = os.getenv('JWT_REFRESH_SECRET_KEY')


@dataclass
class UserAuthentication:
    password_context = CryptContext(
        schemes=["bcrypt"],
        deprecated="auto"
        )

    def get_hashed_password(self, password:str) -> str:
        return self.password_context.hash(password)

    def verify_password(self, password: str, hashed_pass: str) -> bool:
        return self.password_context.verify(password, hashed_pass)

    def create_access_token(
            self, subject: Dict[str, str], expires_delta: int = None
            ) -> str:

        if expires_delta is not None:
            expires_delta = datetime.utcnow() + expires_delta
        else:
            expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

        to_encode = {"data": subject, "exp": expires_delta}
        encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
        return encoded_jwt

    def create_refresh_token(
            self, subject: Dict[str, Any], expires_delta: int = None
            ) -> str:

        if expires_delta is not None:
            expires_delta = datetime.utcnow() + expires_delta
        else:
            expires_delta = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)

        to_encode = {"data": subject, "exp": expires_delta}
        encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, ALGORITHM)
        return encoded_jwt
    

oauth_bearer = OAuth2PasswordBearer(
    tokenUrl="/user/login"
)

class CheckCurrentUser:

    @staticmethod
    def get_current_user(token: LoginUser = Depends(oauth_bearer)) -> Any:
        try:
            payload = jwt.decode(
                token, JWT_SECRET_KEY, algorithms=[ALGORITHM]
            )
            token_data = LoginUser(
                username=payload['data']['username'],
                password=payload['data']['password'],
                exp=payload['exp']
                )
            
            if datetime.fromtimestamp(token_data.exp) < datetime.now():
                raise HTTPException(
                    status_code = status.HTTP_401_UNAUTHORIZED,
                    detail="Token expired",
                    headers={"WWW-Authenticate": "Bearer"},
                )
        except(JWTError, ValidationError):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )

        return token_data
