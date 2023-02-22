FROM python:3.8.7

WORKDIR /FzFilmyZilla

COPY requirements.txt ./

RUN pip install -r requirements.txt

WORKDIR /app

RUN python3 bot.py

COPY . .

CMD ["nohup", "python3", "bot.py", "&"]
