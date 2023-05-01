FROM python:3.8

WORKDIR /app

COPY requirements.txt /app/

RUN pip install certifi && pip install wtforms && pip install flask_wtf && pip install email_validator && pip install flask_mail && pip install -r requirements.txt

COPY . /app/

EXPOSE 5000

CMD ["python", "app.py"]