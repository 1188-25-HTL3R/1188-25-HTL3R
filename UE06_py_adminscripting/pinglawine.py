__author__ = "Luka Pacar"

import subprocess
import ipaddress

def ping_address(address: str):
    """
    Pings the given address

    :param address: The address to be pinged
    """
    _ = subprocess.run(["ping", address], creationflags=subprocess.CREATE_NEW_CONSOLE)

def ping_network(network: str):
    """
    Pings every host in the given Network

    :param network: The network to be pinged
    """
    for host in ipaddress.IPv4Network(network, strict=False).hosts():
        ping_address(str(host))

if __name__ == "__main__":
    ping_network("10.2.3.0/24")