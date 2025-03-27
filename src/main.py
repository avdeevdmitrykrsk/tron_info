from fastapi import FastAPI
from fastapi_pagination import add_pagination

from src.app.api.routers import main_router
from src.app.core.config import setup_logging

app = FastAPI()
app.include_router(main_router)

add_pagination(app)

logger = setup_logging()
