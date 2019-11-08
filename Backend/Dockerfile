FROM python:3

WORKDIR /usr/backend/

ENV FLASK_APP=notes-backend

COPY /requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY /src/ ./

CMD ["flask", "run", "--host", "0.0.0.0"]