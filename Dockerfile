FROM python:3.9-slim

# Install system dependencies for tesseract
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Set environment variable for port
ENV PORT=5000

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "src/app.py"]
