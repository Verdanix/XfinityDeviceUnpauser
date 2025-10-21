#!/bin/bash
# Check that `ip link` is available
if ! command -v ip >/dev/null 2>&1 || ! ip link show >/dev/null 2>&1; then
  echo "error: 'ip link' is not available" >&2
  exit 1
fi

# Accept parameters
if [ $# -lt 2 ]; then
  echo "usage: $0 <interface> <mac_address>" >&2
  exit 2
fi

INTERFACE="$1"
MAC_ADDRESS="$2"

# Validate interface exists
if ! ip link show dev "$INTERFACE" >/dev/null 2>&1; then
  echo "error: interface '$INTERFACE' not found" >&2
  exit 3
fi

# Basic MAC address validation
if ! [[ "$MAC_ADDRESS" =~ ^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$ ]]; then
  echo "error: invalid MAC address format" >&2
  exit 4
fi

sudo ip link set dev "$INTERFACE" down
sudo ip link set dev "$INTERFACE" address "$MAC_ADDRESS"
sudo ip link set dev "$INTERFACE" up
