# Libraries
import argparse
# Custom functions
import web, scan

# Globals
TARGETS = ""
VHOST_FILE = ""
VHOSTS = []
DOMAIN = ""
IPS = []
WEBSERVERS = []
EXCLUSIONS_FILE = ""
EXCLUSIONS = []

def main():
    # Parse arguments
    global VHOST_FILE, TARGETS, DOMAIN, IPS, WEBSERVERS
    getArgs()

    # Scanning Ports
    IPS = scan.getIPsFromRange(TARGETS)
    print(IPS)
    #WEBSERVERS = scan.findWebservers(IPS)

    # Scanning Web Servers
    
    return

def getArgs():
    global VHOST_FILE, TARGETS, DOMAIN, EXCLUSIONS_FILE, EXCLUSIONS
    # Setup argument parser
    parser = argparse.ArgumentParser(prog="Eternal", description="External Network Enumeration Suite", epilog="Made by @OfficialScragg", usage="\n\teternal -d example.com -v vhosts.txt -t 127.0.0.1-127.0.0.100\n\teternal -d example.com -v vhosts.txt -t 127.0.0.1/24\n", add_help=True, allow_abbrev=True)
    parser.add_argument("-d", "--domain", help="Primary domain of the target organisation.", required=True)
    parser.add_argument("-v", "--vhosts", help="File containing a list of VHOSTs associated with the organisation", required=True)
    parser.add_argument("-t", "--targets" , help="Target IP ranges in CIDR or hyphonated format comma separated.", required=True)
    parser.add_argument("-x", "--exclude", help="File containing hosts to exlude from target range.")
    # Parse arguments and populate globals
    args = parser.parse_args()
    VHOST_FILE = args.vhosts
    TARGETS = args.targets
    DOMAIN = args.domain
    EXCLUSIONS_FILE = args.exclude
    # Read files and populate arrays
    if VHOST_FILE != None:
        with open(VHOST_FILE, 'r') as v:
            for host in v.read().split("\n"):
                VHOSTS.append(host)
    if EXCLUSIONS_FILE != None:
        with open(EXCLUSIONS_FILE, 'r') as v:
            for host in v.read().split("\n"):
                EXCLUSIONS.append(host)

if __name__ == "__main__":
    main()