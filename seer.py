import ipinfo
import nmap
import whois
import socket

# ASCII banner with your name
ascii_banner = """
\033[96m___  ___  ___  ___    ___  _ _    ___  _ _  ___  ___  ___  ___   ___  _ _ 
|  _]| . || . \| __]  | . ]| | |  |  _]| | || . ]| __]| . \/  _] | __]| \ |
| [__| | || | || _]   | . \\   /  | [__\   /| . \| _] |   /| [_/\| _] |   |
`___/`___'|___/|___]  |___/ |_|   `___/ |_| |___/|___]|_\_\`____/|___]|_\_|
                                                                           
                                                
\033[0m****************************************************************
* Created by \033[94mWinston Ighodaro\033[0m                                  *
* \033[94mhttps://www.cybergeneration.tech\033[0m                             *
* \033[94mhttps://www.tiktok.com/cybergen2\033[0m                             *
****************************************************************
                                      
"""

print(ascii_banner)

# access token for ipinfo.io, put yours here
access_token = '09d8c3fe6f8ed9'

# create a client object with the access token
handler = ipinfo.getHandler(access_token)

# Get the user's IP address
user_ip = socket.gethostbyname(socket.gethostname())

# Print user's IP address
print(f"Your IP address: \033[92m{user_ip}\033[0m")

# Function to print action
def print_action(action):
    print(f"\n\033[95m{action}...\033[0m")

# ask the user for the IP address to lookup
ip_address = input("Enter the IP address you want to locate: ")

# get the ip info
print_action("Performing IP lookup")
details = handler.getDetails(ip_address)

# print the ip info
for key, value in details.all.items():
    print(f"\033[93m{key}:\033[0m {value}")

# run a very fast nmap scan to detect open ports
print_action("Scanning for open ports")
scanner = nmap.PortScanner()
scanner.scan(ip_address, arguments='-T4 -F')

# print the results of the nmap scan
for host in scanner.all_hosts():
    print('\033[94mHost :\033[0m %s (%s)' % (host, scanner[host].hostname()))
    print('\033[94mState :\033[0m %s' % scanner[host].state())
    for proto in scanner[host].all_protocols():
        print('\033[94mProtocol :\033[0m %s' % proto)
        lport = scanner[host][proto].keys()
        for port in lport:
            print('\033[94mport :\033[0m %s\t\033[94mstate :\033[0m %s' % (port, scanner[host][proto][port]['state']))

# WHOIS lookup with exception handling
print_action("Performing WHOIS lookup")
try:
    w = whois.whois(ip_address)
    print("\n\033[94mWHOIS Information:\033[0m")
    print(w)
except Exception as e:
    print("\033[91mError occurred while performing WHOIS lookup:\033[0m", e)