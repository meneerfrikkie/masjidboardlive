FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the updated script to the container
COPY main.py /app/main.py

# Set environment variables (defaults, if any)
ENV POLL_INTERVAL=600  # Optional default polling interval

# Set the command to run the script
CMD ["python", "/app/main.py"]
