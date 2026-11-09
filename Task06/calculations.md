# Task 6 – Detailed Analysis and Calculations

## 1. Given Ethernet Port Report

| Parameter | Reported Value |
|---|---:|
| Speed | 100 Mbps |
| Duplex | Half |
| Auto-negotiation | Off |
| Link detected | Yes |
| RX errors | 2,381 |
| Late collisions | 412 |
| CRC errors | 1,907 |

## 2. Error Analysis

Late collisions occur when a collision is detected outside the normal collision-detection window in a half-duplex Ethernet environment. They can indicate a duplex mismatch or a physical network problem.

CRC errors occur when a received frame fails the Cyclic Redundancy Check, indicating possible corruption during transmission.

The combination of late collisions and CRC errors suggests a possible duplex mismatch between the PC and switch.

## 3. Configuration Correction

The PC is operating at 100 Mbps half-duplex, while the gigabit switch port is configured for auto-negotiation.

The recommended correction is to enable auto-negotiation on both ends.

Linux command:

`sudo ethtool -s eth0 autoneg on`

The interface name must be replaced with the actual interface name. The switch port should also be configured for auto-negotiation.

## 4. MAC Address Analysis

### Address: 01:00:5e:0a:01:02

This is a multicast/group MAC address. The prefix 01:00:5e is used for IPv4 multicast Ethernet addresses.

### Address: 3c:52:82:4e:11:07

The first three bytes, 3C:52:82, represent the OUI. It identifies the manufacturer or assignee of the MAC address block.

## 5. Jumbo Frame Analysis

Jumbo frames support larger Ethernet payloads, commonly around 9,000 bytes.

They can reduce per-frame processing overhead and improve bulk CCTV storage transfers.

However, all devices along the communication path must support the configured MTU, including network adapters, switches and routers where applicable.

Jumbo frames do not automatically solve congestion or insufficient bandwidth.

## 6. Ring and Star Comparison

A ring topology with fast recovery can redirect traffic through an alternate path after a cable failure, depending on the ring protocol.

In a star topology, a cable failure normally disconnects the devices connected through that link. Failure of the central switch can affect all connected devices.

Exact recovery times depend on the selected ring protocol and switch configuration; the assignment does not specify these values.

## 7. Result

The Ethernet report indicates a likely duplex mismatch. Enabling auto-negotiation on both ends is the recommended correction. The MAC addresses, jumbo-frame requirements and effects of a cable failure in ring and star topologies were analysed.