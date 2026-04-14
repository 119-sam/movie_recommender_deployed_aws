FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install --default-timeout=100 --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "Home.py", "--server.port=8501", "--server.address=0.0.0.0"]