# ---- Base Image ----
FROM python:3.11-slim

# ---- Environment variables ----
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ---- Set working directory ----
WORKDIR /app

# ---- Install system dependencies ----
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# ---- Copy requirements first (for caching) ----
COPY requirements.txt .

# ---- Install Python dependencies ----
RUN pip install --no-cache-dir -r requirements.txt

# ---- Copy project files ----
COPY . .

# ---- Expose Streamlit port ----
EXPOSE 8501

# ---- Run Streamlit app ----
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]