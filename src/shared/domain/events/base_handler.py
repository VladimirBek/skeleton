from abc import ABC, abstractmethod

from src.shared.domain.events.domain_event import DomainEvent


class BaseHandler(ABC):

    @abstractmethod
    async def __call__(self, event: DomainEvent):
        raise NotImplementedError()
