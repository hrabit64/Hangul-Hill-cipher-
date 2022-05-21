import numpy as np
from dotenv import load_dotenv
import os

load_dotenv()


def convert(K: np.array, target: str, N: int = 2) -> str:
    """
    make target text convert using hill cipher
    :param K: hip cipher key
    :param target: plain text or cipher text
    :param N: block size
    :return: converted text
    """
    if len(target) % N:
        while len(target) % N:
            target += " "

    res = ""

    for i in range(0, len(target), N):
        char_matrix = []

        for j in range(N):
            char_matrix.append(ord(target[i + j]) - int(os.environ["BASE"]) if not target[i + j] == " " else int(
                os.environ["MOD"]) - 1)

        char_matrix = np.array(char_matrix)
        idx_matrix = K @ char_matrix % int(os.environ["MOD"])
        res = res + "".join(
            map(lambda x: chr(int(x) + int(os.environ["BASE"])) if not int(x) == int(os.environ["MOD"]) - 1 else " ",
                idx_matrix))

    return res
