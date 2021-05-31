FROM node:15-alpine as static
WORKDIR /app
COPY /client/package*.json ./
RUN npm install
COPY ./client/ .
RUN npm run build

FROM python:3 as server
ENV PYTHONUNBUFFERED=1
ENV MONGO_HOST=items_db
WORKDIR /app
COPY ./backend/requirements.txt /app/
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install -r requirements.txt
COPY ./backend/ /app/
COPY ./mongo_client.py /usr/local/lib/python3.8/dist-packages/pymongo/mongo_client.py
COPY --from=static /app/dist/inventorybase/static/css /app/inventorybase/static/css
COPY --from=static /app/dist/inventorybase/static/js /app/inventorybase/static/js
COPY --from=static /app/dist/index.html /app/templates/
#ENTRYPOINT ["gunicorn", "--env", "DJANGO_SETTING_MODULE=deploy.deploy_settings", "backend.wsgi:application", "-b", "0.0.0.0:8000"]
ENTRYPOINT ["./manage.py", "runserver", "0.0.0.0:8000"]
