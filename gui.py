import tkinter as tk
from tkinter import scrolledtext
from tools.ip_checker import check_ip_address
from tools.connection_test import test_ipv6_connectivity
import subprocess

# Function to check IP address type
def check_ip():
    ip = entry.get()
    result = check_ip_address(ip)
    result_label.config(text=f"IP Address Type: {result}")

# Function to test IPv6 connectivity with the given host
def run_connectivity_test():
    output_text.delete(1.0, tk.END)
    host = host_entry.get()
    if not host:
        output_text.insert(tk.END, "Please enter a host to test connectivity.\n")
        return

    output_text.insert(tk.END, f"Testing IPv6 Connectivity to {host}...\n")
    try:
        result = test_ipv6_connectivity(host)
        output_text.insert(tk.END, f"Connectivity test result for {host}: {result}")
    except Exception as e:
        output_text.insert(tk.END, f"Error during connectivity test: {e}")

# Function to run tunneling simulation
def run_tunneling_sim():
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, "Running Tunneling Simulation...\n")
    try:
        result = subprocess.run(
            ["python", "./transition/tunneling_sim.py"], capture_output=True, text=True
        )
        output_text.insert(tk.END, result.stdout)
        if result.stderr:
            output_text.insert(tk.END, f"Error: {result.stderr}")
    except Exception as e:
        output_text.insert(tk.END, f"Exception occurred: {e}")

# Function to run dual-stack simulation
def run_dual_stack_sim():
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, "Running Dual-Stack Simulation...\n")
    try:
        result = subprocess.run(
            ["python", "./transition/dual_stack_sim.py"], capture_output=True, text=True
        )
        output_text.insert(tk.END, result.stdout)
        if result.stderr:
            output_text.insert(tk.END, f"Error: {result.stderr}")
    except Exception as e:
        output_text.insert(tk.END, f"Exception occurred: {e}")

# Function to run IPv4 to IPv6 conversion simulation
def run_ipv4_to_ipv6_conversion():
    output_text.delete(1.0, tk.END)
    ipv4_address = ipv4_entry.get()
    if not ipv4_address:
        output_text.insert(tk.END, "Please enter an IPv4 address to convert.\n")
        return

    output_text.insert(tk.END, f"Converting IPv4 address {ipv4_address} to IPv6...\n")
    try:
        result = subprocess.run(
            ["python", "./tools/v4tov6.py", ipv4_address], capture_output=True, text=True
        )
        output_text.insert(tk.END, result.stdout)
        if result.stderr:
            output_text.insert(tk.END, f"Error: {result.stderr}")
    except Exception as e:
        output_text.insert(tk.END, f"Exception occurred: {e}")

# Initialize the GUI window
app = tk.Tk()
app.title("IPv6 Transition Toolkit")
app.geometry("500x600")  # Increased height for better layout

# IP Checking Section
tk.Label(app, text="Enter IP address:").pack(pady=5)
entry = tk.Entry(app)
entry.pack()

check_button = tk.Button(app, text="Check IP", command=check_ip)
check_button.pack(pady=5)

result_label = tk.Label(app, text="")
result_label.pack(pady=5)

# Connectivity Test Section
tk.Label(app, text="Enter Host for IPv6 Connectivity Test:").pack(pady=5)
host_entry = tk.Entry(app)
host_entry.pack()

connectivity_button = tk.Button(app, text="Test IPv6 Connectivity", command=run_connectivity_test)
connectivity_button.pack(pady=5)

# Buttons for Tunneling, Dual-Stack, and IPv4 to IPv6 Conversion
tunneling_button = tk.Button(app, text="Run Tunneling Simulation", command=run_tunneling_sim)
tunneling_button.pack(pady=5)

dual_stack_button = tk.Button(app, text="Run Dual-Stack Simulation", command=run_dual_stack_sim)
dual_stack_button.pack(pady=5)

# Section for IPv4 to IPv6 conversion
tk.Label(app, text="Enter IPv4 address to convert to IPv6:").pack(pady=5)
ipv4_entry = tk.Entry(app)
ipv4_entry.pack()

convert_button = tk.Button(app, text="Convert IPv4 to IPv6", command=run_ipv4_to_ipv6_conversion)
convert_button.pack(pady=5)

# Output Area
output_text = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=60, height=15, font=("Arial", 10))
output_text.pack(pady=10)

# Start the GUI loop
app.mainloop()
