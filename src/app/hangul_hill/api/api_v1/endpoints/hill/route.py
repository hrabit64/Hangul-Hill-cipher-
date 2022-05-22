import numpy as np
from fastapi import APIRouter

from app.hangul_hill.api.api_v1.endpoints.hill.hillcipher import hill_encryption, hill_decryption
from app.hangul_hill.api.api_v1.endpoints.hill.keygenerator import get_random_key
from app.hangul_hill.api.api_v1.endpoints.hill.validation import validation_string, validation_key
from app.hangul_hill.schemas.hill import encryptionRequest, encryptionResponse, decryptionResponse, decryptionRequest,generateKeyResponse
from app.hangul_hill.utils.exceptions.exception import NotValidTextError, NotValidKeyError

hill_route = APIRouter(prefix="/hill")


@hill_route.post("/encryption", response_model=encryptionResponse)
async def create_encryption(req: encryptionRequest):
    """
    make plain text to cipher text using hill cipher.
    """
    key = np.array([[req.a, req.b], [req.c, req.d]])
    plain_text = req.plain_text.strip().replace("\n"," ")

    if not validation_key(key):
        raise NotValidKeyError()

    if not validation_string(plain_text):
        raise NotValidTextError

    return {"cipher_text": hill_encryption(key, plain_text)}


@hill_route.post("/decryption", response_model=decryptionResponse)
async def create_decryption(req: decryptionRequest):
    """
    make cipher text to plain text using hill cipher.
    """
    key = np.array([[req.a, req.b], [req.c, req.d]])
    cipher_text = req.cipher_text.strip().replace("\n", " ")

    if not validation_key(key):
        raise NotValidKeyError()

    if not validation_string(cipher_text):
        raise NotValidTextError

    return {"plain_text" : hill_decryption(key, cipher_text)}


@hill_route.get("/randomkey", response_model=generateKeyResponse)
async def get_randomkey():
    """
    make random key, it's 2*2 matrix
    """
    rand_key = get_random_key()

    return {"a": rand_key[0][0],
            "b": rand_key[0][1],
            "c": rand_key[1][0],
            "d": rand_key[1][1]}