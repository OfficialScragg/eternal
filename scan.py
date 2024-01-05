import subprocess, ipaddress

# Take user input and determine individual target IPs
def getIPsFromRange(iprange):
    ips = []
    # Determine format of input
    print("Determining IPs from range", iprange)
    try:
        netIpv4Address = ipaddress.ip_network(iprange)
    except Exception as e:
        iprange = iprange.split("")+"."+iprange.split(".")[]
    # traversing through the above IPv4 addresses list
    for i in netIpv4Address:
        # printing the current IPv4 address
        ips.append(i)
    return ips

# Scan target IP for webserver ports
def findWebservers(ips):
    # Add IPs to text file

    # Execute Nmap scan for common web ports

    # Scrape Nmap output for webservers
    print("Scanning", ips, "for webserver ports")
    return
