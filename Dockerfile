COPY requirements.txt /requirements.txt
RUN cd /
RUN pip3 install -U pip && pip3 install -U -r requirements.txt
RUN mkdir /FzFilmyZilla
WORKDIR /FzFilmyZilla
COPY start.sh /start.sh
CMD ["/bin/bash", "/start.sh"]
