FROM python:3.12-slim
WORKDIR /app
COPY . .
EXPOSE 8000
RUN pip install pytest
CMD ["python3", "app/main.py"]
