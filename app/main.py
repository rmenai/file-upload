from app.apps import app, v1
from app.constants import Settings

from fastapi import Depends, File, UploadFile, HTTPException
from fastapi.security.api_key import APIKey
from fastapi.staticfiles import StaticFiles

from app.utils.api_key import api_key_handler
from app.utils.file import FileHandler

from starlette.responses import RedirectResponse, Response
from starlette.requests import Request
from starlette.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND


@app.get("/")
async def root():
    """Redirects main url to docs"""
    return RedirectResponse(url=f"/{Settings.api_path}/docs")


@v1.get("/")
async def root_api():
    """Redirects main url to docs"""
    return RedirectResponse(url=f"/{Settings.api_path}/docs")


@v1.post("/upload")
async def upload_file(request: Request, key: APIKey = Depends(api_key_handler.verify),
                      file: UploadFile = File(...), folder: str = ""):
    """Saves the file in the server"""
    file = FileHandler(file)

    await file.write(folder=folder)

    return {
        "id": file.id,
        "url": file.get_url(request.base_url._url)
    }


@v1.delete("/delete", response_class=Response, status_code=HTTP_204_NO_CONTENT)
async def delete_file(id: str, key: APIKey = Depends(api_key_handler.verify)):
    """Removes the file from the server"""
    if file := FileHandler.files.get(id):
        await file.delete()
    else:
        raise HTTPException(HTTP_404_NOT_FOUND, "Couldn't find the file")


app.mount(f"/{Settings.api_path}", v1)

# Opens the files folder
app.mount(f"/{Settings.files_url_path}", StaticFiles(directory=Settings.upload_path), name="files")
