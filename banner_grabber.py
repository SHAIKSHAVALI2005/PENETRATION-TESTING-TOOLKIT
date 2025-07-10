import socket

def grab(ip, port=80):
    try:
        s = socket.socket()
        s.connect((ip, port))
        s.send(b"HEAD / HTTP/1.0\r\n\r\n")
        banner = s.recv(1024)
        print("[+] Banner:")
        print(banner.decode(errors="ignore"))
        s.close()
    except Exception as e:
        print(f"[-] Failed to grab banner: {e}")
