# set relevant python version
FROM python:3.9

# set working directory
WORKDIR /app

# Copy your analysis microservice script into the container
COPY . /app/

# install system dependencies for matplotlib
RUN apt-get update && apt-get install -y \
    libfreetype6-dev \
    libxft-dev \
    libpng-dev \
    pkg-config \
    python3-tk

# install required Python packages
RUN pip install -r requirements.txt

# Define the entry point (replace with your actual script name)
CMD ["sleep", "infinity"]

