FROM python:3.11-slim
WORKDIR /app
COPY generator.py analyzer.py .
CMD ["python", "generator.py"]
