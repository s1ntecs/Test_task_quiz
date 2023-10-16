from pydantic import BaseModel, validator
from sqlalchemy import Column, String, Integer

from db.db import Base


class QuestionData(BaseModel):
    questions_num: int

    @validator("questions_num")
    def check_questions_num(cls, value):
        if value <= 0:
            raise ValueError("questions_num должен быть больше 0")
        return value


class Question(Base):
    __tablename__ = "question_list"

    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)
    created_at = Column(String)

    def __repr__(self):
        return (f"quiz_id: {self.id}\nquestion: {self.question}\n"
                f"answer: {self.answer}\ncreated_at: {self.created_at}")
