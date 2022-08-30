FROM python:3.9

COPY . /app
ENV PYTHONPATH /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "app/main.py"]
