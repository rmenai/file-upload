from fastapi import UploadFile
from app.constants import Settings

import random
import string
import aiofiles
import re
import os


class FileHandler:
    files = {}

    def __init__(self, file: UploadFile):
        self.file = file
        self.filename = file.filename
        try:
            self.extension = re.findall(r"\..+", self.filename)[-1]
        except IndexError:
            self.extension = ""

        self.id = FileHandler.generate_id()
        self.path = None

        self.url = ""

    @staticmethod
    def generate_id():
        """Generates a random file id"""
        return "".join(random.choices(string.ascii_lowercase + string.digits, k=Settings.id_lenght))

    async def write(self, folder=""):
        """Writes the file locally"""

        # Removes additional slashes
        while "//" in folder:
            folder = folder.replace("//", "")
        if folder == "/":
            folder = ""

        if folder:
            try:
                os.makedirs(f"{Settings.upload_path}/{folder}")
            except OSError:
                pass

            self.path = f"{folder}/{self.id}{self.extension}"  # Example: img/photo.png
        else:
            self.path = f"{self.id}{self.extension}"  # Example: file.txt

        async with aiofiles.open(f"{Settings.upload_path}/{self.path}", "wb") as f:
            content = await self.file.read()
            await f.write(content)

        FileHandler.files[self.id] = self

    def get_url(self, base_url: str):
        """Returns the url of the file"""
        return f"{base_url[:-1]}/{Settings.files_url_path}/{self.path}"

    async def delete(self):
        """Deletes the file locally"""
        try:
            os.remove(f"{Settings.upload_path}/{self.path}")
        except OSError:
            raise FileNotFoundError
