# Task 12 – Re-evaluate and Adapt the Network Design

## 1. Assumption for AGV traffic

The assignment specifies 50 AGVs but does not provide their command size or transmission interval.

For estimation, each AGV is assumed to use the Task 1 robot-controller traffic pattern:

- Command size = 200 bytes
- Transmission interval = 2 ms

Traffic per AGV:

= (200 × 8) / 0.002  
= 800,000 bits/s  
= 0.8 Mbps

Traffic for 50 AGVs:

= 50 × 0.8  
= 40 Mbps

## 2. Revised plant traffic

Original eight-line plant traffic = 1,265.92 Mbps

Additional AGV traffic = 40 Mbps

Revised traffic:

= 1,265.92 + 40  
= **1,305.92 Mbps = 1.30592 Gbps**

This estimate assumes the 50 AGVs are additional to the original eight-line traffic.

## 3. Handover calculation

Route length = 1,200 m  
AGV speed = 2 m/s

Trip duration:

= 1,200 / 2  
= 600 seconds = 10 minutes

### Wi-Fi

Access-point spacing = 30 m

Coverage areas = 1,200 / 30 = 40

Assuming 39 transitions:

Total interruption = 39 × 150 ms  
= 5,850 ms = **5.85 seconds**

### Private 5G

Cell coverage = 300 m

Coverage areas = 1,200 / 300 = 4

Assuming 3 transitions:

Total interruption = 3 × 20 ms  
= 60 ms

### Deadline comparison

Required command deadline = 10 ms

- Wi-Fi handover = 150 ms, which is 15 times the deadline.
- 5G handover = 20 ms, which is 2 times the deadline.

Private 5G improves mobility but the stated handover time still exceeds the command deadline.

## 4. Five-plant estimate

Assuming each of five plants has the same 50 AGVs:

Revised traffic per plant = 1.30592 Gbps

Five-plant traffic:

= 1.30592 × 5  
= **6.5296 Gbps**

A redundant 10 Gbps or higher fibre backbone is recommended as a starting point, with capacity headroom.

## 5. Final decision

Decision: MODIFY the original design.

- Retain shielded Ethernet for fixed robot control.
- Introduce private 5G for AGVs.
- Use Wi-Fi 6 for office users.
- Retain fibre for the backbone.
- Use CRC for error detection and suitable FEC where supported.
- Apply QoS, redundant paths and local fail-safe control for critical commands.

The calculations are estimates based on the stated assumptions. Actual command traffic, latency and handover performance must be measured during deployment.