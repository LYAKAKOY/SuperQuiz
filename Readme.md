# Супер Викторина
Api для викторины

## Стек программы
FastApi, PostgresSql

## Как запустить проект
1. Требуется сделать git clone проекта
```bash
git clone https://github.com/LYAKAKOY/SuperQuiz.git
```
2. Перейти в папку SuperQuiz
```bash
cd SuperQuiz 
```
3. Собрать и запустить docker-compose.yaml
```bash
docker compose -f docker-compose.yaml up -d 
```
4. Сделать миграции внутри контейнера backend с помощью alembic
```bash
docker-compose run --rm backend sh -c 'alembic upgrade heads'
```
## Documentation
После запуска будет доступна
[Documentation](http://localhost:8000/docs) по адресу http://localhost:8000/docs