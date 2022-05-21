import re
import os

import numpy as np
from dotenv import load_dotenv

from app.hangul_hill.api.api_v1.endpoints.hill.cal import modular_multiplicative_inverse, det

load_dotenv()

def validation_string(target:str) -> bool:
    if re.match('[^ 가-힣+]', target) is not None:
        return False

    return True


def validation_key(key: np.array) -> bool:
    if np.linalg.det(key) != 0:
        if modular_multiplicative_inverse(det(key), int(os.environ["MOD"])):
            return True

    return False

