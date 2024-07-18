FROM python:3.12.4-alpine

WORKDIR /app

RUN pip install poetry
COPY pyproject.toml /app/
RUN poetry update

CMD [ "poetry", "run", "python", "src/main.py" ]
