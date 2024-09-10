# classifier docker
FROM python:3.11

WORKDIR /code

COPY src/fishregression/main_classifier.py /code/main_classifier.py
COPY src/fishregression/data/classifier.pkl /code/data/classifier.py

RUN pip install --no-cache-dir --upgrade git+https://github.com/NishNovae/fishregression.git@main

CMD ["uvicorn", "main2:app", "--host", "0.0.0.0", "--port", "8080"]
