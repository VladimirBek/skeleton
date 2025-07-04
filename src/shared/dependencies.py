"""
    Dependencies which can be used for DI
"""
from functools import lru_cache

from src.shared.config import Settings
from src.shared.domain.events.event_dispatcher import EventDispatcher


@lru_cache()
def get_settings():
    return Settings()


@lru_cache(maxsize=1)
def get_event_dispatcher_singleton() -> EventDispatcher:
    """Создает единственный экземпляр EventDispatcher"""
    dispatcher = EventDispatcher()
    print(f"Created singleton EventDispatcher with ID: {id(dispatcher)}")
    return dispatcher
