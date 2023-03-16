FROM python:3.11-slim-buster

WORKDIR /src

COPY requirements.txt /src

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY app /src/app

EXPOSE $PORT

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "$PORT"]