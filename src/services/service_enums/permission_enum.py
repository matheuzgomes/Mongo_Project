from enum import Enum


class PermissionEnum(str, Enum):
    ADMIN = 'ADMIN'
    USER = 'USER'
    RESPONSABILITY_CHAIN = ['ADMIN','USER']