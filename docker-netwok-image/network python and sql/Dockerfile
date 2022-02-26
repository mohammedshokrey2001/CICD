FROM python

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install mysql-connector-python
RUN pip install mysqlclient

CMD [ "python", "script.py" ]


