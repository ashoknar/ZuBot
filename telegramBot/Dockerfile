FROM python:3.8.16-slim-buster

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY *.py ./
COPY model/ ./model
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./bot.py" ]
