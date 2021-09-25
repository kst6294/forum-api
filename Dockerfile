FROM python:3.7

MAINTAINER ANDY

ENV PYTHONUNBUFFERED 1

# Set a Working Directory
WORKDIR /app/

# Install Production Dependecies First
COPY requirements/ /app/requirements/
RUN pip install --no-cache-dir -r requirements/requirements-dev.txt

COPY . /app/

ARG PORT=8000
ENV PORT $PORT
EXPOSE $PORT 8001 8002

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]
