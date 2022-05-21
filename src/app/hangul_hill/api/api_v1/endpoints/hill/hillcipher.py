import numpy as np

from app.hangul_hill.api.api_v1.endpoints.hill.cal import get_inv_k
from app.hangul_hill.api.api_v1.endpoints.hill.convert import convert
from app.hangul_hill.utils.log import logger


def hill_encryption(key:np.array,plain_text:str) -> str:
    """
    make plain text to cipher text by 'hill cipher'
    :param key: hill cipher key, it's must det(key) != 0 and it has modular multiplicative inverse
    :param plain_text: it's must be hangul with complete text, ex) "안녕하세요" , "히오스" don't be like 'jamo' ex) "ㄱ","ㅗ"
    """
    logger.info(f"encryption // key : {key} // plain_text : {plain_text}")
    return convert(key,plain_text)


def hill_decryption(key:np.array,cipher_text:str) -> str:
    """
    make cipher text to plain text by 'hill cipher'
    :param key: hill cipher key, it's must det(key) != 0 and it has modular multiplicative inverse
    :param cipher_text: it's must be hangul with complete text, ex) "안녕하세요" , "히오스" don't be like 'jamo' ex) "ㄱ","ㅗ"
    """

    inv_key = get_inv_k(key)
    logger.info(f"decryption // key : {inv_key} // cipher_text : {cipher_text}")
    return convert(inv_key,cipher_text)