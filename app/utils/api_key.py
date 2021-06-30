from fastapi import HTTPException
from starlette.status import HTTP_403_FORBIDDEN

from typing import Union
from app.constants import Settings

import secrets


class ApiKey:
    """Handler for api keys"""

    def __init__(self, api_key: str):
        self.key = api_key

    @staticmethod
    def generate_key(length):
        return secrets.token_urlsafe(length)

    async def verify(self, key: str) -> Union[str, HTTPException]:
        """Verify the validity of the api key"""

        if key == self.key:
            return key
        else:
            raise HTTPException(
                status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials."
            )


api_key_handler = ApiKey(Settings.api_key)
