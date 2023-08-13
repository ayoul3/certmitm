FROM python:3.9-slim

# Create a directory for our application
WORKDIR /app

# Install required libraries
RUN pip install dnspython

# Copy the script to the container
COPY dns_server.py /app/

# Run the script
CMD ["python", "/app/dns_server.py"]
