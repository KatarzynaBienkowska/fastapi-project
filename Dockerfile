FROM python:3.10-alpine
WORKDIR /code

COPY code/requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt

RUN set PYTHONPATH=.
COPY code/main.py /code

EXPOSE 9000
ENTRYPOINT ["uvicorn"]
CMD ["main:app", "--host", "0.0.0.0", "--port", "9000"]