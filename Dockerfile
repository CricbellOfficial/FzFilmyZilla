FROM python:3.8.7

WORKDIR /TamilanBotsZ

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY ..

CMD ["python3", "bot.py"]
