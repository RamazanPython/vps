FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ARG APP_USER=vps
RUN groupadd -r ${APP_USER} && useradd --no-log-init -r -g ${APP_USER} ${APP_USER}

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential git \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # gunicorn installation \
  && apt-get install -y gunicorn \
  # Install opencv python dependencies
  && apt-get install ffmpeg libsm6 libxext6  -y \
  # Install zbar for qr reads
  && apt-get install -y libzbar0 \
  # Translations dependencies
  && apt-get install -y gettext \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*


RUN pip install --upgrade pip pipenv
COPY Pipfile* ./
RUN pipenv install --system --ignore-pipfile --dev

WORKDIR /usr/src/app

COPY entrypoint.sh .
RUN chmod +x ./entrypoint.sh

COPY ./project/ .


ENTRYPOINT ["./entrypoint.sh"]
