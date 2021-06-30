import os


class Settings:
    api_key = os.environ.get("API_KEY")
    api_path = "api/v1"
    upload_path = "app/uploads"

    files_url_path = "files"

    id_lenght = 10
