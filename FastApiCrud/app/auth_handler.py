import time
from typing import Dict

import jwt
# from decouple import config


JWT_SECRET = "dab38ab4823a241c558abcf3146adba8d983fcf2cd98b0b7"
JWT_ALGORITHM = "HS256"


def token_response(token: str):
    return {
        "access_token": token
    }



def signJWT(user_id: str) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "expires": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}