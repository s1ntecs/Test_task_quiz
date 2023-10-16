# Test_task_quiz

## Тестовое задание на вакансию Python разработчик в компании Bewise.ai.

### Описание
Тестовое задание выполнено согласно техническому заданию.

### Запуск приложения
Для запуска приложения выполните следующие действия:

1. Склонируйте репозиторий:

    ```sh
    git clone https://github.com/s1ntecs/Test_task_quiz.git
    ```

2. Установите Docker и Docker-compose.

   - Инструкция по установке Docker в Linux: [Установка Docker в Linux](https://docs.docker.com/engine/install/)

   - Инструкция по установке Docker Compose в Linux: [Установка Docker Compose в Linux](https://docs.docker.com/compose/install/)

3. Создайте файл `.env` и добавьте в него следующие переменные среды (пример):

    ```
    POSTGRES_DSN=postgresql+asyncpg://postgres:postgres@db:5432/quiz
    POSTGRES_PASSWORD=postgres
    POSTGRES_USER=postgres
    POSTGRES_DB=quiz
    ```

4. Разверните приложение с помощью docker-compose, выполнив следующую команду:

    ```sh
    docker-compose -f docker-compose.yaml up --build
    ```

5. Отправьте POST-запрос с количеством необходимых вопросов для викторины:

    ```sh
    curl -X POST -H "Content-Type: application/json" -d '{
        "questions_num": 1
    }' http://localhost:8080/quiz
    ```

    Пример запроса:

    ```json
    {
        "questions_num": 0
    }
    ```

6. После обработки запроса вы получите одну викторину.

### Документация API
Используйте [документацию API](http://localhost:8080/api/openapi) для выполнения запросов и ознакомления с функциональностью приложения.
