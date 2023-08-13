# `certmitm` Tool

`certmitm` is a tool designed to demonstrate and test vulnerabilities in applications that fail to properly validate TLS certificates. By taking advantage of these vulnerabilities, an attacker might intercept and manipulate traffic, compromising the integrity and confidentiality of the data.

## Purpose

Many mobile applications utilize Transport Layer Security (TLS) as a standard to establish secure communication channels for transmitting sensitive data. These channels are considered secure, primarily due to the trust model around certificates. However, if an application fails to validate these certificates correctly, it opens up a vulnerability that can be exploited.

This tool aims to highlight these vulnerabilities, providing security professionals a mechanism to test applications and thereby encouraging developers to adopt proper TLS validation methods.

## Credits

The `certmitm` tool was created by aapooksman, and this repository seeks to provide instructions and context for its usage.

## Prerequisites

- Docker installed on your machine.

## How to Use

1. **Clone the Repository**:

```bash
   git clone https://github.com/Roni-Carta/certmitm
```

2. **Navigate to the Tool Directory**:

```bash
cd certmitm
```
3. **Build and Start the Tool**:

```bash
docker-compose up --build
```

4. **Setup and Test**: Ensure that the server and the device you're testing are on the same network. Set up the device's DNS to the server's IP. For example, if your server IP is 192.168.1.16, set this IP as the DNS in the device settings.

5. **Test the Application**: Download and install the application you wish to test. Start the application. If you don't notice any logs on your server, try restarting the application a few times.

6. **Review Logs**: When the vulnerability is triggered, you should observe logs in your server's console, which will provide insight into the intercepted traffic.

**Note**: Always ensure you have permission to test the application, and never use this tool for malicious intent.