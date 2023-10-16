from fastapi import Depends
from sqlalchemy import insert, select
from sqlalchemy.sql import exists
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm.exc import NoResultFound

from typing import Dict, Union, Optional
from .common import DBObjectService
from models.quiz import Question
from db.db import get_session


class SaveService(DBObjectService):
    async def save(self,
                   question_data: Dict
                   ) -> Optional[bool]:
        """ Метод который сохраняет новую викторину в БД. """
        result = await self.db_session.execute(
            insert(Question).values(
                id=question_data["id"],
                question=question_data["question"],
                answer=question_data["answer"],
                created_at=question_data["created_at"]
            )
        )
        return result

    async def get(self, question_id: int) -> Union[bool, Question]:
        """ Метод который получает викторину в БД по его id. """
        try:
            result = await self.db_session.execute(
                select(Question).filter(Question.id == question_id)
                )
            return result.scalar()
        except NoResultFound:
            return False

    async def is_exist(self, question_id: int) -> bool:
        """ Метод который проверяет наличие викторины в БД по его id. """
        try:
            result = await self.db_session.execute(
                select(exists().where(Question.id == question_id))
            )
            return result.scalar()
        except NoResultFound:
            return False


def get_user_service(
        db_session: AsyncSession = Depends(get_session)
) -> SaveService:
    return SaveService(db_session)
