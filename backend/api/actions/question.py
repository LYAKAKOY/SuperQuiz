from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from api.schemas import ShowQuestion
from db.dals import QuestionDAL
from quiz.quiz_questions import get_questions


async def _create_new_questions(questions_num: int, session: AsyncSession) -> None:
        new_questions = await get_questions(questions_num)
        for question in new_questions:
            async with session.begin():
                question_dal = QuestionDAL(session)
                created_question = await question_dal.create_question(
                    id_question=question.get('id'),
                    text_question=question.get('question'),
                    text_answer=question.get('answer'),
                    created_at=datetime.strptime(question.get('created_at'), '%Y-%m-%dT%H:%M:%S.%fZ')
                )
                if created_question is None:
                    while created_question is not None:
                        additional_question = await get_questions(1)
                        created_question = await question_dal.create_question(
                            id_question=additional_question[0].get('id'),
                            text_question=additional_question[0].get('question'),
                            text_answer=additional_question[0].get('answer'),
                            created_at=datetime.strptime(additional_question[0].get('created_at'), '%Y-%m-%dT%H:%M:%S.%fZ')
                        )

async def _get_last_question(session: AsyncSession) -> ShowQuestion | None:
    async with session.begin():
        question_dal = QuestionDAL(session)
        last_question = await question_dal.get_last_question()
        if last_question is not None:
            return ShowQuestion(
            id_question=last_question.id_question,
            text_question=last_question.text_question,
            text_answer=last_question.text_answer,
            created_at=last_question.created_at
        )
        return