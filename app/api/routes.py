from fastapi import APIRouter

from app.models.schemas import QuestionRequest, AnswerResponse
from app.rag.rag_service import ask_question

router = APIRouter()


@router.get("/health")
def health_check():
    return {"status": "ok"}


@router.post("/ask", response_model=AnswerResponse)
def ask(request: QuestionRequest):
    answer = ask_question(request.question)

    return AnswerResponse(answer=answer)