# TODO: Install the backend dependency package into the app folder inside the container.

FROM python:3.11

WORKDIR /app

COPY src ./src
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000",  "--reload"]