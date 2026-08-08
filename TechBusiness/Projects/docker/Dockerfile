FROM python:3.12-alpine
WORKDIR /app
COPY .. /app
RUN python3 -m pip install --no-cache-dir flask
EXPOSE 8000
CMD ["python3", "-m", "http.server", "8000"]
