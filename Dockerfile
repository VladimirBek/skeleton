FROM python:3.12

COPY ./requirements.txt /tmp/
WORKDIR /app

RUN pip install --no-cache-dir --upgrade -r /tmp/requirements.txt
COPY . /app
ENV PYTHONPATH=/app

RUN apt-get update && apt-get install -y curl apt-utils apt-transport-https debconf-utils gcc build-essential g++ && rm -rf /var/lib/apt/lists/*

RUN curl https://packages.microsoft.com/keys/microsoft.asc | tee /etc/apt/trusted.gpg.d/microsoft.asc && curl https://packages.microsoft.com/config/ubuntu/22.04/prod.list | tee /etc/apt/sources.list.d/mssql-release.list

RUN apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql18 mssql-tools18 unixodbc-dev

CMD alembic upgrade head && \
    uvicorn src.shared.entrypoints.fastapi_app:app --host 0.0.0.0 --port 8000