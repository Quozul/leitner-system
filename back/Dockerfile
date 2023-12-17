FROM python:3.12-alpine

WORKDIR /src/app

RUN pip install --upgrade pip
RUN pip install "uvicorn[standard]"

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

CMD uvicorn main:app --port 8080 --host 0.0.0.0
