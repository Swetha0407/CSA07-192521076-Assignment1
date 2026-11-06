# Task 1 – Traffic Sizing Calculations

## 1. Given Data

| Device Category | Number of Devices | Traffic per Device |
|---|---:|---:|
| Robot controllers | 40 | 200 bytes every 2 ms |
| Vibration sensors | 600 | 50 bytes/sec |
| CCTV cameras | 24 | 4 Mbps |
| Office users | 150 | 2 Mbps each (10% active at peak) |

## 2. Traffic Calculation for One Production Line

### A. Robot Controllers

Each robot controller sends 200 bytes every 2 milliseconds.

- Convert bytes into bits: 200 × 8 = 1600 bits
- Convert interval into seconds: 2 ms = 0.002 seconds

Traffic per robot:

1600 / 0.002 = 800,000 bits/sec = **0.8 Mbps**

For 40 robot controllers:

40 × 0.8 = **32 Mbps**

### B. Vibration Sensors

Each sensor generates 50 bytes per second.

Traffic per sensor:

50 × 8 = 400 bits/sec

For 600 sensors:

600 × 400 = 240,000 bits/sec = **0.24 Mbps**

### C. CCTV Cameras

Each CCTV camera generates 4 Mbps.

For 24 cameras:

24 × 4 = **96 Mbps**

### D. Office Users

Total office users = 150

Active users at peak = 150 × 10% = 15 users

Traffic generated:

15 × 2 = **30 Mbps**

## 3. Total Traffic for One Production Line

Total traffic = Robot traffic + Sensor traffic + CCTV traffic + Office traffic

= 32 + 0.24 + 96 + 30

**Total = 158.24 Mbps**

## 4. Traffic for Eight Production Lines

Assuming all eight production lines generate the same traffic:

158.24 × 8 = **1265.92 Mbps**

Therefore:

**Total traffic = 1.26592 Gbps**

## 5. Identifying the Highest Traffic Source

| Device Category | Traffic |
|---|---:|
| Robot controllers | 32 Mbps |
| Vibration sensors | 0.24 Mbps |
| CCTV cameras | 96 Mbps |
| Office users | 30 Mbps |

CCTV cameras generate the highest traffic at **96 Mbps per production line**.

Robot controllers have the strictest timing requirement, with commands required within **10 ms**.

## 6. Checking the 1 Gbps Uplink

### For One Production Line

Utilisation = (158.24 / 1000) × 100

= **15.824%**

A 1 Gbps uplink is sufficient for one production line under the given traffic assumptions.

### For Eight Production Lines

Required traffic = 1265.92 Mbps

Since 1265.92 Mbps exceeds 1000 Mbps, a single 1 Gbps uplink is insufficient for eight production lines.

Required utilisation = **126.592%**

## 7. Effect of FIFO Queuing

If robot commands and CCTV video packets share a single First-In-First-Out (FIFO) queue, robot commands may have to wait behind large video packets.

This can increase queuing delay and jitter. As robot commands have a strict 10 ms deadline, excessive waiting may cause commands to arrive late.

A Quality of Service (QoS) mechanism with priority queuing can help prioritise time-critical robot traffic over less time-sensitive traffic.

## 8. Ranking the Impact of Network Delay

1. **Robot controllers:** Delayed commands may affect machine coordination and production operations because of the strict 10 ms deadline.
2. **Vibration sensors:** Delayed sensor readings may postpone fault detection and predictive maintenance.
3. **CCTV cameras:** Delayed video may affect real-time monitoring.
4. **Office users:** Delays may affect routine activities such as email and ERP access, but generally have less immediate production impact.

This ranking assumes vibration sensors are used for monitoring and not as a separate hard-real-time safety shutdown system.

## 9. Effect of Motion-Triggered CCTV Recording

If CCTV cameras transmit video only 5% of the time:

Revised CCTV traffic = 96 × 0.05

= **4.8 Mbps**

Revised total traffic per production line:

32 + 0.24 + 4.8 + 30

= **67.04 Mbps**

For eight production lines:

67.04 × 8 = **536.32 Mbps**

Therefore, under the motion-triggered recording assumption, the total estimated traffic for eight lines is **536.32 Mbps**, which is within the nominal capacity of a 1 Gbps uplink.

However, protocol overhead, traffic bursts, redundancy and future expansion must also be considered.

## 10. Final Results

| Parameter | Calculated Value |
|---|---:|
| Total traffic per production line | 158.24 Mbps |
| Total traffic for eight lines | 1265.92 Mbps |
| Highest traffic source | CCTV – 96 Mbps |
| Strictest delay requirement | Robot controllers – 10 ms |
| One-line utilisation of 1 Gbps link | 15.824% |
| Eight-line utilisation of 1 Gbps link | 126.592% |
| Revised one-line traffic with motion-triggered CCTV | 67.04 Mbps |
| Revised eight-line traffic | 536.32 Mbps |

**Note:** These calculations represent estimated application-level traffic based on the values provided in the assignment. Protocol overhead and additional network capacity margins are not included.