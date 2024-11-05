import subprocess
import platform

def setup_tunneling():
    print("Setting up IPv4-over-IPv6 and IPv6-over-IPv4 Tunneling...")

    # Step 1: IPv6-over-IPv4 Tunnel Simulation
    print("\nStep 1: Configuring IPv6-over-IPv4 Tunnel...")
    try:
        if platform.system() == "Windows":
            # Windows Tunnel Setup Command (Simulated as Windows requires specific network interface config)
            ipv6_over_ipv4_command = [
                "netsh", "interface", "ipv6", "add", "v6v4tunnel",
                "TeredoTunnel", "192.0.2.1", "198.51.100.1"
            ]
        else:
            # Linux/MacOS Tunnel Setup Command (Example - requires root privileges)
            ipv6_over_ipv4_command = [
                "sudo", "ip", "tunnel", "add", "sit1", "mode", "sit", "remote",
                "198.51.100.1", "local", "192.0.2.1", "ttl", "255"
            ]

        # Execute tunnel setup command
        result_ipv6_over_ipv4 = subprocess.run(ipv6_over_ipv4_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        if result_ipv6_over_ipv4.returncode == 0:
            print("IPv6-over-IPv4 tunnel configured successfully.")
        else:
            print("Failed to configure IPv6-over-IPv4 tunnel:", result_ipv6_over_ipv4.stderr)
    
    except Exception as e:
        print("Error during IPv6-over-IPv4 tunnel setup:", e)

    # Step 2: IPv4-over-IPv6 Tunnel Simulation
    print("\nStep 2: Configuring IPv4-over-IPv6 Tunnel...")
    try:
        if platform.system() == "Windows":
            # Windows - Enable Teredo as an alternative
            ipv4_over_ipv6_command = [
                "netsh", "interface", "ipv6", "set", "teredo", "enterpriseclient"
            ]
        else:
            # Linux/MacOS Tunnel Setup Command (Example)
            ipv4_over_ipv6_command = [
                "sudo", "ip", "tunnel", "add", "sit0", "mode", "gre6", "remote",
                "2001:db8::2", "local", "2001:db8::1", "ttl", "255"
            ]

        # Execute tunnel setup command
        result_ipv4_over_ipv6 = subprocess.run(ipv4_over_ipv6_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        if result_ipv4_over_ipv6.returncode == 0:
            print("IPv4-over-IPv6 tunnel configured successfully.")
        else:
            print("Failed to configure IPv4-over-IPv6 tunnel:", result_ipv4_over_ipv6.stderr)
    
    except Exception as e:
        print("Error during IPv4-over-IPv6 tunnel setup:", e)

    print("\nTunneling setup complete. Ensure that the remote and local IP addresses are correct for your network configuration.")

if __name__ == "__main__":
    setup_tunneling()
