FROM python:3.6.10

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000

COPY . /app

RUN python nltk_initialize.py

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
