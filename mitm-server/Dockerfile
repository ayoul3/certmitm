# Base Image
FROM python:3.10-slim-buster

# Maintainer
LABEL maintainer="youremail@example.com"

# Install necessary utilities
RUN apt-get update && \
    apt-get install -y iproute2 dnsmasq iptables && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Setting work directory in container
WORKDIR /certmitm

# Copying requirements file to container
COPY requirements.txt .

# Installing python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copying other required files and directories
COPY certmitm.py .
COPY certmitm certmitm/
COPY real_certs real_certs/


# Command to run the application
CMD ["python3", "certmitm.py", "--listen", "443", "--workdir", "testing", "--verbose", "--show-data"]
