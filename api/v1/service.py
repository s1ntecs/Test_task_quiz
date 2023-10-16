from typing import Union

from fastapi import (APIRouter,
                     status,
                     Depends,
                     Response)

from services.save_quiz import get_user_service, SaveService
from models.quiz import QuestionData, Question
from services.quiz import get_questions_data

router = APIRouter()


@router.post('/quiz',
             description='get quiz',
             status_code=status.HTTP_201_CREATED,
             response_model=None)
async def save(question_data: QuestionData,
               save_service: SaveService = Depends(get_user_service)
               ) -> Question:
    # Количество требуемых викторин
    count = question_data.questions_num

    # Запускаем в цикле пока не получим необходимое количество викторин
    while count > 0:
        # Получаем викторины из сервиса jservice.io
        questions_data, status_code = await get_questions_data(count)
        if status_code != 200:
            e_msg = f"Ошибка в сервисе jservice.io status_code={status_code}"
            return Response(status_code=500, content=e_msg)
        # Обнуляем количество необходимых новых викторин
        count = 0
        try:
            for i, question_data in enumerate(questions_data):
                if i % 100 == 0:
                    await save_service.db_session.commit()
                # Проверяем наличие викторины в БД
                existing_question = await save_service.is_exist(
                    question_data["id"])
                # Если есть в БД тогда прибавляем count
                if existing_question:
                    count += 1
                    continue
                # Создаем новую викторину
                result = await save_service.save(question_data)
                # При успешном создании сохраняем в quiz_id
                if result:
                    quiz_id = question_data["id"]
            # Сохраняем транзакцию в БД
            await save_service.db_session.commit()
        except Exception:
            return Response(status_code=500)
    try:
        # Отправляем последнюю созданную викторину
        last_result = await save_service.get(quiz_id)
    except Exception:
        return Response(status_code=204)
    return last_result
