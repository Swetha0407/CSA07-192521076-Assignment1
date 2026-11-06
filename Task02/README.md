# Task 2 – Collision Domains, Broadcast Domains and Network Standards

## 1. Aim

To analyse the contractor's network topology, calculate the number of collision and broadcast domains, identify the OSI layers of the networking devices, classify the connections and examine the importance of standard-compliant networking equipment.

## 2. Given Network Topology

The contractor's proposed office network consists of:

- Three hubs, each connecting 8 PCs.
- All three hubs connected to a single 24-port switch.
- The first switch connected to router interface G0/0.
- Router interface G0/1 connected to a second switch.
- The second switch connected to 12 IP phones.

## 3. Network Topology Diagram

```text
       8 PCs             8 PCs             8 PCs
         |                 |                 |
      [Hub 1]           [Hub 2]           [Hub 3]
         |                 |                 |
         +-----------------+-----------------+
                           |
                    [Switch 1]
                           |
                       Router G0/0
                       [ ROUTER ]
                       Router G0/1
                           |
                    [Switch 2]
                     /  /  |  \
                12 IP Phones
```

## 4. Collision Domain Calculation

A collision domain is a network segment in which devices share the same transmission medium and simultaneous transmissions may result in collisions.

A hub operates at the Physical Layer (Layer 1) and repeats incoming signals to all connected ports. Therefore, all devices connected to the same hub share one collision domain.

A switch operates at the Data Link Layer (Layer 2) and creates a separate collision domain for each active port.

| Network Segment | Collision Domains |
|---|---:|
| Hub 1 with 8 PCs | 1 |
| Hub 2 with 8 PCs | 1 |
| Hub 3 with 8 PCs | 1 |
| Switch 1 to router G0/0 | 1 |
| Switch 2: 12 IP phone ports and 1 router uplink | 13 |
| **Total** | **17** |

**Total collision domains = 17**

## 5. Broadcast Domain Calculation

A broadcast domain is a logical network segment in which broadcast frames can reach all devices without crossing a router.

The router separates the network into two broadcast domains:

1. The network connected to router interface G0/0, containing the first switch and the three hub segments.
2. The network connected to router interface G0/1, containing the second switch and the 12 IP phones.

**Total broadcast domains = 2**

This calculation assumes that each router interface belongs to a single VLAN/subnet and that no additional VLAN segmentation is configured.

## 6. OSI Layers of Networking Devices

| Device | OSI Layer | Function |
|---|---|---|
| Hub | Layer 1 – Physical | Repeats electrical signals without examining frames or MAC addresses. |
| Switch | Layer 2 – Data Link | Forwards Ethernet frames using MAC addresses. |
| Router | Layer 3 – Network | Routes packets between networks using IP addresses. |
| PC | Layers 1–7 | Uses the complete network stack for communication. |
| IP Phone | Layers 1–7 | Uses Ethernet, IP and application protocols for voice communication. |

### Why a Hub Cannot Stop Collisions

A hub does not maintain a MAC address table or make forwarding decisions. It simply repeats an incoming signal to all other ports. All connected devices share the same collision domain. Consequently, simultaneous transmissions can collide, and the hub cannot isolate one device's traffic from another.

## 7. Point-to-Point and Multipoint Connections

**Multipoint connection:**

The PCs connected to each hub share a common transmission medium. Each hub segment therefore represents a multipoint communication arrangement.

**Point-to-point connections:**

- Switch 1 to router interface G0/0.
- Router interface G0/1 to Switch 2.
- Each IP phone connected to an individual switch port.

Switched Ethernet connections provide dedicated links between the connected devices.

## 8. Network Standards and Defining Organisations

| Technology / Model | Standard | Defining Organisation |
|---|---|---|
| Ethernet | IEEE 802.3 | IEEE – Institute of Electrical and Electronics Engineers |
| Wi-Fi | IEEE 802.11 | IEEE – Institute of Electrical and Electronics Engineers |
| IPv4 | RFC 791 | IETF – Internet Engineering Task Force |
| OSI Reference Model | ISO 7498 | ISO – International Organization for Standardization |
| 5G | 3GPP specifications and ITU IMT-2020 framework | 3GPP and ITU-R |

## 9. Importance of Standard-Compliant Equipment

The plant should purchase standard-compliant networking equipment for the following reasons:

1. **Interoperability:** Devices manufactured by different vendors can communicate using common protocols.
2. **Reliability:** Standardised communication procedures provide predictable network behaviour.
3. **Compatibility:** New equipment can be integrated with the existing network infrastructure.
4. **Scalability:** The network can be expanded without depending entirely on a single manufacturer.
5. **Maintenance:** Standard-compliant equipment has wider technical support and easier troubleshooting.

## 10. Alternative Concept Analysis – Replacing Hubs with Unmanaged Switches

If the three hubs are replaced with three unmanaged switches, each replacement switch connects 8 PCs and one uplink to the central switch.

Each replacement switch creates 9 collision domains:

8 PC connections + 1 uplink connection = 9 collision domains.

For three replacement switches:

3 × 9 = 27 collision domains.

The remaining connections are:

- Switch 1 to router G0/0 = 1 collision domain.
- Switch 2 with 12 IP phone ports and one router uplink = 13 collision domains.

Therefore:

Total collision domains = 27 + 1 + 13

**Total collision domains = 41**

The broadcast domains remain unchanged at 2, assuming the same VLAN arrangement.

| Parameter | Original Network | Alternative Network |
|---|---:|---:|
| Collision domains | 17 | 41 |
| Broadcast domains | 2 | 2 |

### Evaluation

Replacing hubs with unmanaged switches increases the number of collision domains from 17 to 41. Each PC receives a separate switched link, reducing collisions and improving bandwidth utilisation.

However, unmanaged switches do not automatically divide the network into separate broadcast domains. Broadcast frames can still reach all devices within the same VLAN.

Therefore, replacing hubs with switches improves collision isolation and network efficiency, but VLAN configuration or Layer 3 segmentation would be required to create additional broadcast domains.

## 11. Result

The contractor's original network contains **17 collision domains and 2 broadcast domains**. The hubs operate at OSI Layer 1, switches operate at Layer 2 and routers operate at Layer 3.

Replacing the three hubs with unmanaged switches increases the collision domains to **41**, while the broadcast domains remain **2**. Standard-compliant equipment is recommended to ensure interoperability, reliability, compatibility and future scalability.