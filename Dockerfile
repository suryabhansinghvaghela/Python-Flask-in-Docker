FROM python:3-alphine

MAINTAINER Suryabhan Singh Vaghela


COPY . /app

WORKDIR /app


RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["main.py"]