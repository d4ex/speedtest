FROM python:3.8-slim

WORKDIR /usr/local/bin

RUN pip install prometheus_client
RUN pip install speedtest-cli

COPY metrics-exporter.py .

RUN chmod +x metrics-exporter.py

EXPOSE 8000

CMD ["python3", "-u", "metrics-exporter.py"]
