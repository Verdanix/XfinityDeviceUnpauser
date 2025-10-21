from src.mac_changer import get_mac_address, get_octets_from_range, new_mac_address

mac_address = get_mac_address()


def test_octets_retriever():
    first_3_octets = get_octets_from_range(mac_address, 0, 3)
    last_3_octets = get_octets_from_range(mac_address, 3, 6)
    assert len(first_3_octets) == 6
    assert len(last_3_octets) == 6
    assert first_3_octets != last_3_octets
    assert first_3_octets == mac_address[2:8]
    assert last_3_octets == mac_address[8:14]


def test_octets_incrementer():
    last_3_octets = get_octets_from_range(mac_address, 3, 6)
    incremented_value = int(last_3_octets, 16) + 1
    incremented_hex = hex(incremented_value)[2:]
    assert len(incremented_hex) <= 6
    assert incremented_hex != last_3_octets


def test_new_mac_address():
    new_address = new_mac_address()
    assert len(new_address) == 12
    assert new_address != mac_address
