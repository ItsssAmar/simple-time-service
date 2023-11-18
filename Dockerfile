FROM python:3.9-slim

WORKDIR /usr/src/app

COPY app.py .

RUN pip install flask

RUN addgroup -g 1001 -S appuser && \
    adduser -u 1001 -S appuser -G appuser

RUN chown -R appuser:appuser /usr/src/app

USER appuser

EXPOSE 5000

CMD ["python", "app.py"]
