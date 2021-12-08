FROM python:3.10

RUN adduser --disabled-password --home /home/container container

USER container

ENV  USER=container HOME=/home/container

WORKDIR /home/container

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY main.py .

CMD ["python3", "main.py"]
