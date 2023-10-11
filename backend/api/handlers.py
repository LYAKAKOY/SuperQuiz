from logging import getLogger
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from api.actions.question import _create_new_questions, _get_last_question
from api.schemas import ShowQuestion
from db.session import get_db

logger = getLogger(__name__)

quiz_router = APIRouter()


@quiz_router.post("/", response_model=ShowQuestion | None)
async def create_user(questions_num: int, db: AsyncSession = Depends(get_db)) -> ShowQuestion | None:
    try:
        last_question = await _get_last_question(db)
        await _create_new_questions(questions_num, db)
        return last_question
    except IntegrityError as err:
        logger.error(err)
        raise HTTPException(status_code=503, detail=f"Database error: {err}")



