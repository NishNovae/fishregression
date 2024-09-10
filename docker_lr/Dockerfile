FROM python:3.11

WORKDIR /code

COPY src/fishregression/main.py /code/

RUN pip install --no-cache-dir --upgrade git+https://github.com/NishNovae/fishregression.git@main

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
