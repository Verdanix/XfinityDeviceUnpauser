"""Module to create a new MAC address by incrementing the last three octets of the current MAC address."""

from uuid import getnode as get_mac


def get_mac_address():
    """Retrieve the current MAC address in hexadecimal format."""
    return hex(get_mac())


def get_octets_from_range(mac_address: str, octet_start: int, octet_end: int) -> str:
    """Extract octets from the MAC address based on the provided range.
    Param:
        mac_address (str): The MAC address in hexadecimal
        octet_start (int): The starting octet index (0-based).
        octet_end (int): The ending octet index (0-based, exclusive).
    Returns:
        str: The extracted octets as a concatenated string.
    """
    octet_start = octet_start * 2 + 2
    octet_end = octet_end * 2 + 2
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


def new_mac_address():
    """Generate a new MAC address by incrementing the last three octets of the current MAC address.
    Returns:
        str: The new MAC address in hexadecimal format.
    """
    mac_address = get_mac_address()
    first_three_octets = get_octets_from_range(mac_address, 0, 3)
    last_three_octets = get_octets_from_range(mac_address, 3, 6)
    incremented_last_octets = increment_octet(last_three_octets)
    new_mac = first_three_octets + incremented_last_octets
    return new_mac
