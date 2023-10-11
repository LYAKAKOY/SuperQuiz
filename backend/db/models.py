from sqlalchemy import Column, Text, Integer
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Question(Base):
    __tablename__ = "questions"

    pk = Column(Integer, autoincrement=True, primary_key=True)
    id_question = Column(Integer, primary_key=True, nullable=False)
    text_question = Column(Text, unique=True, nullable=False)
    text_answer = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
