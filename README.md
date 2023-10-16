# create_quiz
## тестовое задание №1 на вакансию Python разработчик,  FastAPI quiz.
### Тестовое задание выполнено согласно ТЗ (как я его понял).
Для запуска приложения необходимо сделать следующие действия:
  1. Скопируйте репозиторий
  ```
  git clone https://github.com/s1ntecs/Test_task_quiz.git
  ```
  2. Установите Docker & Docker-compose
  3. Создайте файл .env пример:
  ```
    POSTGRES_DSN=postgresql+asyncpg://postgres:postgres@db:5432/quiz
    POSTGRES_PASSWORD=postgres
    POSTGRES_USER=postgres
    POSTGRES_DB=quiz
  ```
  4. Разверните приложение с помощью docker-compose, выполнив команду:
  ```
  docker-compose -f docker-compose.yaml up --build
  ```
  5.  Отправьте запрос с количеством необходимых вопросов для викторины.
  ```
  curl -X POST -H "Content-Type: application/json" -d '{
  "questions_num": 1
}' http://localhost:8080/quiz
  ```
        Или
    http://localhost:8080/quiz
    ```
    {
        "questions_num": 0
    }
    ```
   6. После обработки запроса вы получите один опрос.

## Запросы вы можете сделать используя документацию по ссылке 
http://localhost:8080/api/openapi