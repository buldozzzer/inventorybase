FROM node:10-alpine as static
WORKDIR /app
COPY /client/package*.json ./
RUN npm install
COPY ./client/ .
RUN npm run build

FROM snakepacker/python:all as server
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY ./backend/requirements.txt /code/
RUN pip install -r requirements.txt
COPY ./backend/ /code/
COPY --from=static /app/dist/static/js /code/static
COPY --from=static /app/dist/static/css /code/static
COPY --from=static /app/dist/index.html /code/templates/index.html