import logging
from datetime import datetime
from typing import Dict, List, Type, Callable, Awaitable
from src.shared.domain.events.domain_event import DomainEvent

date = datetime.today().strftime("%Y-%m-%d")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[logging.StreamHandler()],
)


class EventDispatcher:
    """Диспетчер доменных событий"""

    def __init__(self):
        # Словарь, где ключи - типы событий, значения - списки обработчиков
        self._handlers: Dict[Type[DomainEvent], List[Callable[[DomainEvent], Awaitable[None]]]] = {}

    def register(self, event_type: Type[DomainEvent], handler: Callable[[DomainEvent], Awaitable[None]]):
        """Регистрация обработчика для конкретного типа события"""
        if event_type not in self._handlers:
            self._handlers[event_type] = []
        self._handlers[event_type].append(handler)
        logging.info(f"Handler {handler.__class__.__name__} registered for {event_type.__name__}")

    async def dispatch(self, event: DomainEvent):
        """Публикация события всем зарегистрированным обработчикам"""
        event_type = type(event)
        logging.info(f"Dispatching event of type {event_type.__name__}, handlers: {self._handlers}")

        if event_type in self._handlers:
            for handler in self._handlers[event_type]:
                try:
                    logging.info(f"Calling handler {handler.__class__.__name__}")
                    await handler(event)
                    logging.info(f"Handler {handler.__class__.__name__} completed successfully")
                except Exception as e:
                    logging.info(f"Error in event handler for {event_type.__name__}: {e}")


