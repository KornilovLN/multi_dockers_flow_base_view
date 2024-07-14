FROM mongo:latest

# Установка необходимых инструментов
RUN apt-get update && apt-get install -y python3 python3-pip

# Установка Python библиотек для работы с MongoDB
RUN pip3 install pymongo

# Копирование скриптов для обработки данных
COPY shared_folder /app

# Открытие порта MongoDB
EXPOSE 27017

# Запуск MongoDB при старте контейнера
CMD ["mongod"]
