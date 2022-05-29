FROM python:3.8-slim-buster

CMD mkdir /app

WORKDIR /app
COPY app.py app.py
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
