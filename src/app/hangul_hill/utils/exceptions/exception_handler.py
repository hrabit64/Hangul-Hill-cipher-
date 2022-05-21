from pydantic import ValidationError

from app.hangul_hill.utils.exceptions.exception import NotValidTextError, NotValidKeyError,TooLongKeyError,TooLongTextError
from fastapi import Request
from fastapi.responses import JSONResponse


def include_exception(app):
    app.add_exception_handler(NotValidTextError, NotValidTextError_exception_handler)
    app.add_exception_handler(NotValidKeyError, NotValidKeyError_exception_handler)
    app.add_exception_handler(ValidationError, ValidationError_exception_handler)


async def NotValidTextError_exception_handler(request: Request, exc: NotValidTextError):
    return JSONResponse(
        status_code=200,
        content={
            "message": "입력된 문장에 사용할 수 없는 문자가 포함되어 있습니다."},
    )


async def NotValidKeyError_exception_handler(request: Request, exc: NotValidKeyError):
    return JSONResponse(
        status_code=200,
        content={
            "message": "사용할 수 없는 Key 입니다. 위 설명을 참고하세요"},
    )

async def ValidationError_exception_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=200,
        content={
            "message": "입력된 키에 숫자 이외의 문자가 들어있거나, 문장에 사용할 수 없는 문자가 포함되어있습니다. 입력된 키와 문장을 다시 확인하세요"},
    )

async def TooLongKeyError_exception_handler(request: Request, exc: TooLongKeyError):
    return JSONResponse(
        status_code=200,
        content={
            "message": "입력된 Key의 길이가 너무 깁니다. 위 설명을 참고하세요"},
    )

async def TooLongTextError_exception_handler(request: Request, exc: TooLongKeyError):
    return JSONResponse(
        status_code=200,
        content={
            "message": "입력된 문장의 길이가 너무 깁니다. 위 설명을 참고하세요"},
    )