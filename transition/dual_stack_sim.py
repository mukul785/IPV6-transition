import ctypes
import sys
import subprocess

def enable_dual_stack():
    """Enable both IPv4 and IPv6 on the specified interface."""
    interface_name = "Wi-Fi"  # Change this to your network interface name if needed
    print("Configuring dual-stack (IPv4 and IPv6)...")

    # Enable IPv4
    print("Enabling IPv4...")
    result_ipv4 = subprocess.run(
        ["netsh", "interface", "ipv4", "set", "interface", interface_name, "enabled"], 
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    if result_ipv4.returncode == 0:
        print("IPv4 enabled successfully.")
    else:
        print("Failed to enable IPv4:", result_ipv4.stderr)

    # Enable IPv6
    print("Enabling IPv6...")
    result_ipv6 = subprocess.run(
        ["netsh", "interface", "ipv6", "set", "interface", interface_name, "enabled"], 
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    if result_ipv6.returncode == 0:
        print("IPv6 enabled successfully.")
    else:
        print("Failed to enable IPv6:", result_ipv6.stderr)

    print("Dual-stack configuration complete. Ensure your router and ISP support IPv6.")

if __name__ == "__main__":
    # Request admin privileges
    print("Requesting admin privileges...")
    if ctypes.windll.shell32.IsUserAnAdmin():
        # If already running as admin, proceed to enable dual-stack
        enable_dual_stack()
    else:
        # Relaunch the script with admin privileges
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join([f'"{__file__}"']), None, 1
        )
        sys.exit()  # Exit the current non-elevated process
