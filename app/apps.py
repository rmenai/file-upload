from fastapi import FastAPI
from content_size_limit_asgi import ContentSizeLimitMiddleware

import logging

logger = logging.getLogger("uvicorn.error")

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
app.add_middleware(ContentSizeLimitMiddleware, max_content_size=52428800)  # Limit file size upload to 50 mb

v1 = FastAPI()
