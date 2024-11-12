import socket

ports = {
    0: "Reserved",
    1: "TCP Port Service Multiplexer",
    5: "Remote Job Entry (RJE)",
    7: "Echo",
    9: "Discard",
    11: "Active Users",
    13: "Daytime",
    15: "Netstat",
    17: "Quote of the Day (QOTD)",
    19: "Character Generator",
    20: "FTP Data Transfer",
    21: "FTP Control",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    37: "Time Protocol",
    42: "WINS",
    43: "WHOIS",
    53: "DNS",
    67: "DHCP Server",
    68: "DHCP Client",
    69: "TFTP",
    79: "Finger",
    80: "HTTP",
    110: "POP3",
    115: "SFTP",
    123: "NTP",
    137: "NetBIOS Name Service",
    138: "NetBIOS Datagram Service",
    139: "NetBIOS Session Service",
    143: "IMAP",
    161: "SNMP",
    162: "SNMP Trap",
    179: "BGP",
    443: "HTTPS",
    445: "SMB",
    514: "Syslog",
    515: "Printer",
    543: "Kerberos",
    563: "NNTPS",
    587: "SMTP Submission",
    631: "IPP",
    993: "IMAPS",
    995: "POP3S",
    1080: "SOCKS",
    1194: "OpenVPN",
    1433: "MSSQL",
    1434: "MSSQL Monitor",
    1701: "L2TP",
    1723: "PPTP",
    3128: "HTTP Proxy",
    3268: "LDAP Global Catalog",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    5060: "SIP",
    5900: "VNC",
    5938: "TeamViewer",
    8080: "HTTP Proxy",
    10000: "Webmin",
    20000: "DNP3",
}

def main():
    try:
        host = input('[+] Enter the site name or IP address: ')
        print ("[+] Scanning Ports!")
        print()
        result = []
        for port in ports:
            s = socket.socket()
            s.settimeout(1)
            try:
                s.connect((host, port))
            except socket.error:
                pass
            else:
                service_name = ports.get(port, "Unknown Service")
                print(f"[+] port:{port}({service_name}) is open")
                result.append(f"{port} {service_name}")
                s.close()
        print()
        print ("[+] Scanning Complete!")
        print()
        user = input("[+] Do you want to save output in file y/n: ")
        if user == 'y':
            path = input("[+] Enter Path to save output (Ex:- C:/): ")
            with open(path+'scanned_ports','a') as f:
                f.write(f"==========>{host}<=========="+'\n')
                for res in result:
                    f.write(res+ '\n')
                print()
                print("[+] File Created")
                
    except Exception as e:
        print(str(e))
            
            
if __name__ == "__main__":
    try:
        while True:
            print()
            ch = int(input("[+] Enter 1 to Scan OR 2 to exit: "))
            if ch == 1:
                main()
            elif ch == 2:
                print("[+] Exitting")
                break
    except Exception as e:
        print(str(e))
