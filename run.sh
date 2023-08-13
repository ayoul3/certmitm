#!/bin/bash

dns=192.168.130.196

echo "[*] Starting the DNS Server"

dnscallback=$dns python3 dns-server/dns_server.py &


echo "[*] Starting the Docker Container"
docker compose up --build
echo "[+] Docker Container started and running in the background"

