FROM python:3.9

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip && \
    pip install certifi && \
    pip install wtforms && \
    pip install flask_wtf && \
    pip install email_validator && \
    pip install flask_mail && \
    pip install --upgrade jinja2 && \
    pip install markupsafe && \
    pip install html5lib && \
    pip install -r requirements.txt 
    
    
COPY . /app/

EXPOSE 5000

CMD ["python", "app.py"]
