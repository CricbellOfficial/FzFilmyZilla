FROM python:3.8.7

WORKDIR /FzFilmyZilla

COPY requirements.txt ./

RUN pip install -r requirements.txt

CMD ["python3", "bot.py"]
