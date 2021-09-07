FROM python:3.8.3-alpine3.12

COPY . /ApiFlask

WORKDIR /ApiFlask

ENV PORT 65432

ENV SUGGESTION_NUMBER 10

EXPOSE $PORT

RUN pip install flask

CMD ["python", "ApiFlask.py"]
