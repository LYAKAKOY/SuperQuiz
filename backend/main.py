from fastapi import FastAPI
from fastapi.routing import APIRouter

from api.handlers import quiz_router

app = FastAPI(title="SuperQuiz")

main_api_router = APIRouter()
main_api_router.include_router(quiz_router, prefix="/quiz", tags=["quiz"])

app.include_router(main_api_router)