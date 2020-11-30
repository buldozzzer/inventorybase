FROM node:10-alpine as client
WORKDIR /app
COPY client .
RUN npm install
RUN npm run build


FROM snakepacker/python:all as builder

RUN python3.7 -m venv /usr/share/python3/venv
RUN /usr/share/python3/venv/bin/pip install -U pip

COPY backend/requirements.txt /mnt/
RUN /usr/share/python3/venv/bin/pip install -Ur /mnt/requirements.txt \
 && file="$(echo "$(cat /usr/share/python3/venv/lib/python3.7/site-packages/pymongo/mongo_client.py)")" \
 && echo "${file}" | sed 's/HOST = "localhost"/HOST = "mongo"/' > /usr/share/python3/venv/lib/python3.7/site-packages/pymongo/mongo_client.py

FROM snakepacker/python:3.7 as api

COPY --from=builder /usr/share/python3/venv /usr/share/python3/venv
COPY backend /usr/share/python3/backend
COPY backend/deploy/settings_deploy.py /usr/share/python3/backend/backend/settings.py
COPY   --from=client /app/dist /vue
COPY backend/deploy/entrypoint /entrypoint
ENTRYPOINT ["/entrypoint"]