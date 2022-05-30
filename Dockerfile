FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

ENV FIREBASE_WEB_API_KEY="<your-web-api-key>"

COPY . .

RUN ["chmod", "+x", "runserver.sh"]
CMD ["./runserver.sh"]
