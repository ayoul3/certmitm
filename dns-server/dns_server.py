import dns.resolver
import dns.query
import dns.zone
from dns.exception import DNSException
from dns.rdatatype import *
from dns.rdataclass import *
from dns.flags import *
import dns.name
import os

def ipv4_to_ipv6(ipv4_addr):
    # Convert IPv4 to IPv6
    # In this case, we are using the IPv4-mapped IPv6 addresses
    return "::ffff:" + ipv4_addr

def dns_response(data):
    request = dns.message.from_wire(data)
    response = dns.message.make_response(request)

    # Retrieve IP from environment variable
    dnscallback_ip = os.environ.get("dnscallback")

    for question in request.question:
        # Creating an answer section for the DNS message.
        if question.rdtype == A:
            rrset = dns.rrset.from_text(question.name, 3600, IN, A, dnscallback_ip)
            response.answer.append(rrset)
        elif question.rdtype == AAAA:
            rrset = dns.rrset.from_text(question.name, 3600, IN, AAAA, ipv4_to_ipv6(dnscallback_ip))
            response.answer.append(rrset)

    return response.to_wire()

if __name__ == "__main__":
    from socket import *

    UDP_IP = "0.0.0.0"
    UDP_PORT = 53

    serverSock = socket(AF_INET, SOCK_DGRAM)
    serverSock.bind((UDP_IP, UDP_PORT))

    print("DNS Proxy running on {}:{}".format(UDP_IP, UDP_PORT))

    try:
        while True:
            data, addr = serverSock.recvfrom(1024)
            response = dns_response(data)
            serverSock.sendto(response, addr)
    except KeyboardInterrupt:
        print("\nDNS Proxy is shutting down.")
    finally:
        serverSock.close()
