from fastapi import FastAPI
from pydantic import BaseModel, field_validator
from contextlib import asynccontextmanager
import re
import uvicorn

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))
from src.chain import build_chain

shopbot_chain = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    global shopbot_chain
    print("Building ShopBot chain...")
    shopbot_chain = build_chain()
    print("ShopBot ready.")
    yield


app = FastAPI(
    title="ShopBot API",
    description="AI-powered product assistant for zUdyog Fashion",
    version="1.0.0",
    lifespan=lifespan,
)


class QuestionRequest(BaseModel):
    question: str
    session_id: str = "default"

    @field_validator("question")
    @classmethod
    def validate_question(cls, v: str) -> str:
        v = v.strip()
        v = v.replace("‘", "'")
        v = v.replace("’", "'")
        v = v.replace("“", '"')
        v = v.replace("”", '"')
        v = v.replace("—", " - ")
        v = v.replace("\u200b", "")

        if not v:
            raise ValueError("Question cannot be empty.")

        if len(v) > 500:
            raise ValueError(
                f"Question too long ({len(v)} characters). Maximum is 500."
            )

        injection_patterns = [
            r"ignore\s+(all\s+)?previous\s+instructions",
            r"you\s+are\s+now\s+",
            r"act\s+as\s+",
            r"system\s+prompt",
            r"forget\s+(everything|all)",
        ]

        for pattern in injection_patterns:
            if re.search(pattern, v, re.IGNORECASE):
                raise ValueError("Invalid question format.")

        return v


class AnswerResponse(BaseModel):
    answer: str
    session_id: str


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "ShopBot",
        "version": "1.0.0",
    }


@app.post("/ask", response_model=AnswerResponse)
def ask_shopbot(payload: QuestionRequest):
    answer = shopbot_chain.invoke(payload.question)

    return AnswerResponse(
        answer=answer,
        session_id=payload.session_id,
    )


if __name__ == "__main__":
    uvicorn.run(
        "src.api:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )