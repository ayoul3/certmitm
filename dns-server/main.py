import socket, os
from dnslib import DNSRecord, RR, A, AAAA
from dnslib.server import DNSServer, DNSHandler, BaseResolver, DNSLogger

class CustomResolver(BaseResolver):
    def __init__(self, ipv4_address):
        self.ipv4_address = ipv4_address
        # Address of a real DNS server for proxying
        self.upstream_dns = ("8.8.8.8", 53)

    def resolve(self, request, handler):
        q = request.q
        domain_name = str(q.qname)

        # A record
        if q.qtype == 1 and "example.com." in domain_name:
            reply = request.reply()
            reply.add_answer(RR(rname=q.qname, rtype=q.qtype, rclass=q.qclass, ttl=60, rdata=A(self.ipv4_address)))
            return reply
        else:
            # Forwarding the DNS request
            proxy = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            try:
                proxy.sendto(request.pack(), self.upstream_dns)
                response, _ = proxy.recvfrom(8192)
                return DNSRecord.parse(response)
            finally:
                proxy.close()

if __name__ == '__main__':
    ipv4_addr = os.environ.get("dnscallback", "172.20.10.8") # Evil MiTM

    resolver = CustomResolver(ipv4_addr)
    server = DNSServer(resolver, port=53, address="0.0.0.0", logger=DNSLogger())

    server.start_thread()

    try:
        print(f"DNS Server started")
        while server.isAlive():
            pass
    except KeyboardInterrupt:
        pass
    finally:
        server.stop()
