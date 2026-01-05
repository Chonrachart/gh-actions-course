FROM python:alpine3.19

WORKDIR /app

COPY requirement.txt .

RUN python3 --version
RUN PIP install --no-cache-dir -r requirement.txt

COPY . .

CMD [ "python", "app/main.py"]