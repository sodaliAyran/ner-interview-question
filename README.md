# ner-interview-question

# WARNING! THIS PROJECT FAILED ME IN MY INTERVIEW USE WITH CAUTION!

## Description

This project is the answer for an interview question.
The question consist from 3 parts.

First part was to study a business case which is answered in [SentimentCase.md](https://github.com/sodaliAyran/ner-interview-question/blob/master/SentimentCase.md)

The second part was to train a Named Entity Recognition model from an open
dataset. I used CRF to answer this one. The code can be found in [src/](https://github.com/sodaliAyran/ner-interview-question/tree/master/src)

The third and final part was to dockerize this model as a Web API. I decided to
use Flask framework for web application. The code for the web service can be
found in [service/](https://github.com/sodaliAyran/ner-interview-question/tree/master/service)

You can build the docker image from inside of service folder by using the
command:

```bash

$ docker build -t ner:0.0.1 .

```

And run it by using the command:

```bash

$ docker run -p 5000:5000 ner:0.0.1

```

You can send requests to this service by using the command:

```bash

$ curl -i POST -H "Content-Type: application/json" -d '{"text": "are there any good romantic comedies right now?"}' localhost:5000/named-entity-recognition

```

You response will be the following

```bash
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 155
Server: Werkzeug/1.0.0 Python/3.6.10
Date: Fri, 13 Mar 2020 19:59:38 GMT

{"entities":["O","O","O","O","B-GENRE","I-GENRE","B-YEAR","I-YEAR","I-YEAR"],
"words":["are","there","any","good","romantic","comedies","right","now","?"]}

```
