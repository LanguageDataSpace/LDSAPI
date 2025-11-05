# pip install PyJWT
import jwt

# pip install python-dotenv
from dotenv import load_dotenv
import os

import requests


class LDSClient:

    def __init__(self):
        # Load environment   variables from .env file
        load_dotenv()  # by default loads from .env in current directory
        self.address = os.getenv("ADDRESS")
        self.token = self._load_jwt_from_file("./token.txt")

    @staticmethod
    def _load_jwt_from_file(filepath):
        with open(filepath, "r") as file:
            token = file.read().strip()

        return token

    def _get_headers(self) -> dict:
        """Return default headers with Authorization."""
        return {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    def get(self, path: str, params=None) -> requests.Response:
        headers = {
            "Authorization": f"Bearer {self.token}"
        }

        url = f"https://{self.address}{path}"
        """Send a GET request."""
        response = requests.get(url, headers=self._get_headers(), params=params)
        response.raise_for_status()
        return response.text
