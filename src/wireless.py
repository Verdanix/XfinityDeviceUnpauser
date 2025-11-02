"""Module to create a new MAC address by incrementing the last three octets of the current MAC address."""

import netifaces as ni


def get_default_gateway() -> str:
    """Retrieves the default network interface name.
    Returns:
        str: The network interface name.
    """
    gateways = ni.gateways()
    gateway = gateways["default"][ni.AF_INET][1]
    return gateway


def get_mac_address() -> str:
    """Retrieve the current MAC address in hexadecimal format.
    Returns:
        str: The current MAC address without colons.
    """
    gateway = get_default_gateway()
    addresses = ni.ifaddresses(gateway)
    return addresses[ni.AF_LINK][0]["addr"].replace(":", "")


def get_octets_from_range(mac_address: str, octet_start: int, octet_end: int) -> str:
    """Extract octets from the MAC address based on the provided range.
    Param:
        mac_address (str): The MAC address in hexadecimal
        octet_start (int): The starting octet index (0-based).
        octet_end (int): The ending octet index (0-based, exclusive).
    Returns:
        str: The extracted octets as a concatenated string.
    """
    octet_start = octet_start * 2
    octet_end = octet_end * 2
    return mac_address[octet_start:octet_end]


def increment_octet(octets: str) -> str:
    """Increment the given octets by 1.
    Param:
        octets (str): Octets to increment.
    Returns:
        str: The incremented octets as a concatenated string.
    """
    octets = "".join(octets)
    incremented_value = int(octets, 16) + 1
    incremented_hex = hex(incremented_value)[2:]
    return incremented_hex


def add_colons_to_mac(mac: str) -> str:
    """Format a MAC address string by adding colons between every two characters.
    Param:
        mac (str): The MAC address string without colons.
    Returns:
        str: The formatted MAC address with colons.
    """
    return ":".join(mac[i : i + 2] for i in range(0, len(mac), 2))


def new_mac_address(colons=True) -> str:
    """Generate a new MAC address by incrementing the last three octets of the current MAC address.
    Returns:
        str: The new MAC address in hexadecimal format.
    """
    mac_address = get_mac_address()
    first_three_octets = get_octets_from_range(mac_address, 0, 3)
    last_three_octets = get_octets_from_range(mac_address, 3, 6)
    incremented_last_octets = increment_octet(last_three_octets)
    new_mac = first_three_octets + incremented_last_octets
    if colons:
        new_mac = add_colons_to_mac(new_mac)
    return new_mac
