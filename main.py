from modules import port_scanner, ssh_bruteforce, dir_bruteforce, banner_grabber, ping_sweep

def main():
    print("""
    === Penetration Testing Toolkit ===
    1. Port Scanner
    2. SSH Brute Forcer
    3. Directory Brute Forcer
    4. Banner Grabber
    5. Ping Sweep
    0. Exit
    """)

    choice = input("Choose an option: ")

    if choice == '1':
        ip = input("Enter target IP: ")
        port_scanner.scan_ports(ip)
    elif choice == '2':
        ip = input("Enter target IP: ")
        username = input("Enter username: ")
        wordlist = input("Enter path to password list: ")
        ssh_bruteforce.ssh_login(ip, username, wordlist)
    elif choice == '3':
        url = input("Enter target URL: ")
        wordlist = input("Enter path to directory wordlist: ")
        dir_bruteforce.bruteforce(url, wordlist)
    elif choice == '4':
        ip = input("Enter target IP: ")
        banner_grabber.grab(ip)
    elif choice == '5':
        subnet = input("Enter subnet (e.g., 192.168.1): ")
        ping_sweep.sweep(subnet)
    else:
        print("Exiting...")

if __name__ == "__main__":
    main()
