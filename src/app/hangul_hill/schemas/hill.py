from pydantic import root_validator

from app.hangul_hill.schemas.orm import OrmBaseModel
from app.hangul_hill.utils.exceptions.exception import TooLongKeyError,TooLongTextError

class encryptionRequest(OrmBaseModel):
    a: int
    b: int
    c: int
    d: int
    plain_text: str

    @root_validator(pre=False)
    @classmethod
    def key_validation(cls, values: dict) -> dict:
        for target in ["a", "b", "c", "d"]:
            if not (values[target] <= 11172 and 0 <= values[target]):
                raise TooLongKeyError()
        return values

    @root_validator(pre=False)
    @classmethod
    def text_validation(cls, values: dict) -> dict:
        if not (len(values["plain_text"]) <= 500):
            raise TooLongTextError()
        return values

class encryptionResponse(OrmBaseModel):
    cipher_text: str

class decryptionRequest(OrmBaseModel):
    a: int
    b: int
    c: int
    d: int
    cipher_text: str

    @root_validator(pre=False)
    @classmethod
    def key_validation(cls, values: dict) -> dict:
        for target in ["a", "b", "c", "d"]:
            if not (values[target] <= 11172 and 0 <= values[target]):
                raise TooLongKeyError()
        return values

    @root_validator(pre=False)
    @classmethod
    def text_validation(cls, values: dict) -> dict:
        if not (len(values["cipher_text"]) <= 500):
            raise TooLongTextError()
        return values

class decryptionResponse(OrmBaseModel):
    plain_text: str

class generateKeyResponse(OrmBaseModel):
    a: int
    b: int
    c: int
    d: int

