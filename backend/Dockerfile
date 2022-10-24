FROM python:3.8-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0:8000"]