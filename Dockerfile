FROM python:3.12-slim

ARG CHUNKSIZE=10
ENV CHUNKSIZE=$CHUNKSIZE

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080
CMD ["uvicorn", "main:api", "--host", "0.0.0.0", "--port", "8080"]
