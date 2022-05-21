from typing import Optional

import numpy as np
from dotenv import load_dotenv
import os

load_dotenv()


def modular_multiplicative_inverse(a: int, m: int) -> Optional[int]:
    """

    cal ax = 1 mod m

    """
    if a > m:
        a = a % m

    for x in range(1, m):
        if ((a % m) * (x % m) % m == 1):
            return x

    return None


def det(matrix: np.array):
    """

    cal det (a), it's only work 2*2 matrix

    det(a) = ad - bc

    """
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def adjoint(matrix: np.array):
    '''

    get adjoint matrix. it's only work 2*2 matrix

    a b => d -b
    c d    -c a

    '''
    return np.array([[matrix[1][1], -matrix[0][1]], [-matrix[1][0], matrix[0][0]]])


def get_inv_k(key: np.array):
    '''

    get inverse key

    ref:https://stackoverflow.com/questions/960190/how-to-calculate-the-inverse-key-matrix-in-hill-cipher-algorithm

    '''
    res = modular_multiplicative_inverse(det(key), int(os.environ["MOD"])) * adjoint(key) % int(os.environ["MOD"])
    return res
