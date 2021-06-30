FROM python:3 as server
ENV PYTHONUNBUFFERED=1
ENV MONGO_HOST=items_db
WORKDIR /app
RUN apt-get update
RUN apt-get install tesseract-ocr -y
RUN apt-get install tesseract-ocr-eng
RUN apt-get install tesseract-ocr-rus
RUN apt-get install tesseract-ocr-osd
RUN apt-get install imagemagick
RUN apt-get install ffmpeg libsm6 libxext6  -y
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
ENTRYPOINT ["gunicorn", "tess_ocr.wsgi:application", "-b", "0.0.0.0:8001"]