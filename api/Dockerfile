FROM python:3.8.5-slim

WORKDIR /usr/src

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["waitress-serve","--call","src.serve:create_app"]