FROM python:3.10
ENV PYTHONUNBUFFERED 1
ENV DEBUG False
COPY requirements.txt /code/requirements.txt
WORKDIR /code
RUN pip install -r requirements.txt
ADD . .
RUN pip install gunicorn 
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "core.wsgi"]