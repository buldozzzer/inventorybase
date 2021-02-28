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
RUN pip install -r requirements.txt
COPY ./backend/ /app/
COPY --from=static /app/dist/inventorybase /app/
COPY --from=static /app/dist/index.html /app/templates/
ENTRYPOINT ["gunicorn", "backend.wsgi:application", "-b", "0.0.0.0:8000"]