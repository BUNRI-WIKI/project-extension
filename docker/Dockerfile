
# Use the official Python 3.10 slim
FROM python:3.10-slim

ENV ACCESS_KEY_ID \ 
    SECRET_ACCESS_KEY

# Update & Install libgl1-mesa-glx
RUN apt update && \
    apt install -y htop libgl1-mesa-glx libglib2.0-0

# Install gcc and python3-dev for building certain Python packages
RUN apt-get update && \
    apt-get install -y \
    gcc python3-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Create working directory
WORKDIR /src

# Copy requirements.txt
COPY ./requirements.txt /src/requirements.txt

# Install dependency
RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

# Copy fastapi folder
COPY ./ /src/

# CMD
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]