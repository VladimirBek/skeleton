import uuid
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class DomainEvent(BaseModel):
    """Базовый класс для всех доменных событий"""
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    occurred_on: datetime = Field(default_factory=datetime.now)
    correlation_id: Optional[str] = None

    model_config = {
        'arbitrary_types_allowed': True
    }
