FROM python:3.9-alpine
LABEL "owner"="David Isaac Survive"
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
CMD [ "python","manage.py","runserver","0.0.0.0:8000"]
