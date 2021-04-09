FROM node:15-alpine as static
WORKDIR /app
COPY /client/package*.json ./
RUN npm install
COPY ./client/ .
RUN npm run build

FROM snakepacker/python:all as server
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY ./backend/requirements.txt /app/
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install -r requirements.txt
COPY ./backend/ /app/
COPY --from=static /app/dist/inventorybase/static/css /app/inventorybase/static/css
COPY --from=static /app/dist/inventorybase/static/js /app/inventorybase/static/js
COPY --from=static /app/dist/index.html /app/templates/
ENTRYPOINT ["gunicorn", "backend.wsgi:application", "-b", "0.0.0.0:8000"]
