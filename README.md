# Запуск проекта в Docker

Для того, чтобы собрать и запустить проект в Docker, выполните следующие шаги:

1. Соберите Docker образ: 

`docker build -t vk_test_task .`

2. Запустите контейнер из образа:

`docker run -it --rm --name running-app vk_test_task`

# Примечание
По умолчанию, запускается файл `classifier.py`. Если вы хотите запустить `ranker.py`, модифицируйте `CMD` в `Dockerfile` соответствующим образом.