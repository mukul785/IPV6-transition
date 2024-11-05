import socket

def check_ip_address(ip_address):
    try:
        socket.inet_pton(socket.AF_INET, ip_address)
        return "IPv4"
    except socket.error:
        try:
            socket.inet_pton(socket.AF_INET6, ip_address)
            return "IPv6"
        except socket.error:
            return "Invalid IP address"

if __name__ == "__main__":
    ip = input("Enter an IP address: ")
    print(f"{ip} is {check_ip_address(ip)}")
