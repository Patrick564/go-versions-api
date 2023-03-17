FROM python:3.11-slim-buster

WORKDIR /src

COPY ./requirements.txt ./

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./app /src/app

# ENV PORT=${PORT}

# EXPOSE ${PORT}

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
