import os

def sweep(subnet):
    print(f"[+] Sweeping {subnet}.0/24")
    for i in range(1, 255):
        ip = f"{subnet}.{i}"
        response = os.system(f"ping -c 1 -W 1 {ip} > /dev/null 2>&1")
        if response == 0:
            print(f"[+] Host Up: {ip}")
