# Task 11 – Defend the Network Design

## Aim
To recommend a reliable, scalable and efficient network design for the smart manufacturing plant using the calculations and results from Tasks 1–10.

## Recommended Design

| Area | Recommended Technology |
|---|---|
| Robot cells | Cat6A S/FTP shielded Ethernet |
| Office to shop-floor connection | Fibre |
| Shop floor to data centre | Multimode fibre |
| Plant to head office | Single-mode fibre |
| Office wireless | Wi-Fi 6 |
| Moving equipment | Private 5G |
| Low-rate sensors | Zigbee / LoRaWAN where suitable |

## Error Control and Flow Control
Ethernet CRC/FCS is recommended for error detection. FEC can be used on suitable time-critical links to reduce dependence on retransmissions. TCP provides reliable delivery for office and head-office traffic.

QoS, VLAN separation and priority queuing should protect robot commands from bulk CCTV and office traffic. Sliding-window flow control is recommended for long-distance communication.

## Scalability
The calculated traffic for one plant is 1.26592 Gbps. For five plants, the aggregate traffic is 6.3296 Gbps. Therefore, a redundant 10 Gbps or higher fibre backbone is recommended, with additional capacity headroom.

With motion-triggered CCTV, the calculated five-plant traffic reduces to 2.6816 Gbps.

## Two Major Risks
1. Wireless handover and congestion may violate the 10 ms robot command deadline.
2. Increasing CCTV and production traffic may cause congestion if backbone capacity and QoS are not planned properly.

## Private 5G Alternative
Private 5G should support moving equipment and AGVs. However, robot control, CCTV storage, data-centre connections and backbone communication should remain on wired Ethernet or fibre wherever possible. Wi-Fi 6 is suitable for office devices, while low-rate sensors may use Zigbee or LoRaWAN.

## Conclusion
A hybrid network using shielded Ethernet, fibre, Wi-Fi 6 and private 5G provides the best balance of reliability, mobility, performance and scalability. A fully wireless design is not recommended because the plant has strict latency requirements and high traffic volumes.