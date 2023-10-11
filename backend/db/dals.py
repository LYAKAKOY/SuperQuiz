from datetime import datetime
from sqlalchemy import select, desc
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import Question


class QuestionDAL:

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def get_last_question(self) -> Question | None:
        query = select(Question).order_by(desc(Question.pk)).limit(1).with_for_update()
        res = await self.db_session.execute(query)
        last_question = res.fetchone()
        if last_question is not None:
            return last_question[0]
        return

    async def create_question(
            self,
            id_question: int,
            text_question: str,
            text_answer: str,
            created_at: datetime
    ) -> Question | None:
        new_question = Question(
            id_question=id_question,
            text_question=text_question,
            text_answer=text_answer,
            created_at=created_at
        )
        try:
            self.db_session.add(new_question)
            await self.db_session.commit()
            await self.db_session.flush()
            return new_question
        except IntegrityError:
            await self.db_session.rollback()
            return
