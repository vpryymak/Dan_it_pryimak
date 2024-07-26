
FROM python:3.9-slim

WORKDIR /app


COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

ENV FLASK_APP=app.py

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
