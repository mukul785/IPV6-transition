import ipaddress
import sys

def convert_ipv4_to_ipv6(ipv4_address):
    # Convert the IPv4 address to an IPv6 mapped address
    ipv4 = ipaddress.IPv4Address(ipv4_address)
    ipv6_mapped = ipaddress.IPv6Address(f"::ffff:{ipv4}")
    return str(ipv6_mapped)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python v4tov6.py <IPv4 address>")
        sys.exit(1)

    ipv4_address = sys.argv[1]
    ipv6_mapped_address = convert_ipv4_to_ipv6(ipv4_address)
    print(f"IPv4 address {ipv4_address} mapped to IPv6 is {ipv6_mapped_address}")
