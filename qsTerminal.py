import subprocess
import platform
import socket
import time
import os

path = 'C:/'
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)

def main():
    print("QStack Terminal [Version 0.1.1]")
    print(host_name)
    print(host_ip)

    while True:
        code = input(">> QS >>>")
        if code == 'qsCheckIP':
            print("Your local IP is: " + host_ip)
            print("Your Desktop Name is: " + host_name)

if __name__ == "__main__":
    main()