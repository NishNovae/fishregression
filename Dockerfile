# regression docker
FROM python:3.11

WORKDIR /code

COPY src/fishregression/main_regressor.py /code/main_regressor.py
COPY src/fishregression/data/regressor.pkl /code/data/regressor.py

RUN pip install --no-cache-dir --upgrade git+https://github.com/NishNovae/fishregression.git@main

CMD ["uvicorn", "main_regressor:app", "--host", "0.0.0.0", "--port", "8080"]
