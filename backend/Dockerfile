#FROM snakepacker/python:all as builder
#
#RUN python3.7 -m venv /usr/share/python3/venv
#RUN /usr/share/python3/venv/bin/pip install -U pip
#
#COPY requirements.txt /mnt/
#RUN /usr/share/python3/venv/bin/pip install -Ur /mnt/requirements.txt \
# && file="$(echo "$(cat /usr/share/python3/venv/lib/python3.7/site-packages/pymongo/mongo_client.py)")" \
# && echo "${file}" | sed 's/HOST = "localhost"/HOST = "mongo"/' > /usr/share/python3/venv/lib/python3.7/site-packages/pymongo/mongo_client.py
#
#FROM snakepacker/python:3.7 as api
#
#COPY --from=builder /usr/share/python3/venv /usr/share/python3/venv
#COPY . /usr/share/python3/backend
#COPY deploy/settings_deploy.py /usr/share/python3/backend/backend/settings.py
#COPY deploy/entrypoint /entrypoint
#ENTRYPOINT ["/entrypoint"]

FROM snakepacker/python:all as builder
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

