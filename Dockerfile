FROM python:3.11.3-slim

WORKDIR Bot/

RUN pip install "poetry==1.3.1"

COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false \
    && poetry install --without dev --no-root


COPY . .
EXPOSE 80

CMD ["python" , "main.py"]