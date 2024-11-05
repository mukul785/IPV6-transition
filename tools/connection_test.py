import subprocess

def test_ipv6_connectivity(host):
    try:
        result = subprocess.run(
            ["ping", host, "-6", "-n", "1"], capture_output=True, text=True
        )
        if result.returncode == 0:
            message = f"IPv6 connectivity to {host} succeeded!"
        else:
            message = f"IPv6 connectivity to {host} failed.\nOutput: {result.stdout}"
    except Exception as e:
        message = f"Error testing {host}: {e}"
    
    print(message)  # For console output
    return message  # For GUI or other uses

if __name__ == "__main__":
    hosts = ["youtube.com", "ipv6-test.com", "facebook.com"]
    for host in hosts:
        result = test_ipv6_connectivity(host)
        # Here `result` will contain the message returned, which could also be passed to GUI elements
