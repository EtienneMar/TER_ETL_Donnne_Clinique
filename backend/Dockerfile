FROM python:3.11.3-alpine

WORKDIR /backend
COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "/backend/app/main.py"]
