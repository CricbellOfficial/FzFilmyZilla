FROM python:3.8.7

WORKDIR /FzFilmyZilla

COPY requirements.txt ./

RUN pip install -r requirements.txt

WORKDIR /app

COPY . .

CMD ["python3", "bot.py"]



