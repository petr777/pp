FROM python:3.7

RUN python -m pip install flask gunicorn flask-restful requests scrapy html-text

WORKDIR /app

ADD main.py main.py

COPY vk_app vk_app

EXPOSE 5000

CMD [ "gunicorn", "--bind", "0.0.0.0:5000", "main:app" ]

