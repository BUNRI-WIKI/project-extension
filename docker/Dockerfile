
# Use the official Python 3.10 slim
FROM python:3.10-slim

# Update & Install libgl1-mesa-glx
RUN apt update && \
    apt install -y htop libgl1-mesa-glx libglib2.0-0

# Create working directory
WORKDIR /src

# Copy requirements.txt
COPY ./requirements.txt /src/requirements.txt

# Install dependency
RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

# Copy fastapi folder
COPY ./app /src/app
