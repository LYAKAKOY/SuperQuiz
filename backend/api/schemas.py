from datetime import datetime
from pydantic import BaseModel


class TunedModel(BaseModel):
    class Config:
        from_attributes = True


class ShowQuestion(TunedModel):
    id_question: int
    text_question: str
    text_answer: str
    created_at: datetime

