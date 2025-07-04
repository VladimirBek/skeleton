import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends
from starlette.middleware.cors import CORSMiddleware

from src.shared.dependencies import get_event_dispatcher_singleton


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Получаем синглтон
    event_dispatcher = get_event_dispatcher_singleton()
    # Регистрируем обработчики
    service_example = ...
    if service_example:
        example_handler = ...
        event_dispatcher.register(
            ...,
            example_handler
        )

    yield


# Create FastAPI application instance
app = FastAPI(
    title="Backoffice API",
    docs_url="/swagger",
    dependencies=[Depends(check_access)],
    lifespan=lifespan
)

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------------------------------- Регистрация роутов ---------------------------------------------------
app.include_router(..., prefix="/api/v1")
