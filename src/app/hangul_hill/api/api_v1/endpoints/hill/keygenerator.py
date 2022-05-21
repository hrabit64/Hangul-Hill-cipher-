import numpy as np
from dotenv import load_dotenv
import os

from app.hangul_hill.api.api_v1.endpoints.hill.validation import validation_key

load_dotenv()


def get_random_key(N: int = 6) -> np.array:
    """
    generate key for hill cipher. it's must be det(key) != 0,and has modular multiplicative inverse
    :param N: key size, it's generate N*N matrix
    :return: key
    """
    while True:
        key = np.random.randint(int(os.environ["MOD"]) - 1, size=N * N).reshape(N, N)
        if validation_key(key) is True:
            return key
