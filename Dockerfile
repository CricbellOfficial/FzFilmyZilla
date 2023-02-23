FROM python:3.10

WORKDIR /FzFilmyZilla

COPY requirements.txt ./

RUN pip install -r requirements.txt

WORKDIR /FzFilmyZilla

COPY . .

CMD ["python3", "bot.py"]
