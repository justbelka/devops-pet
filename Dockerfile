FROM python:3.12

WORKDIR /app

COPY cbs/requirements.txt /app

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY cbs/ /app

COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

RUN useradd -m runuser

RUN chown -R runuser:runuser /app

RUN chown -R runuser:runuser /entrypoint.sh

USER runuser
