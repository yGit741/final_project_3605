# set relevant python version
FROM python:3.9

# set working directory
WORKDIR /app

# Copy your analysis microservice script into the container
COPY . /app/

# install required Python packages
RUN pip install -r requirements.txt

EXPOSE 80

# Define the entry point (replace with your actual script name)
CMD ["python", "main.py"]

