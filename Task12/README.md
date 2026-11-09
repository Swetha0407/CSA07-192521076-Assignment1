# Task 12 – Re-evaluate and Adapt the Network Design

## Aim
To evaluate the original smart manufacturing network after introducing private 5G and 50 autonomous guided vehicles (AGVs), and recommend the required modifications.

## A. Impact Analysis
The original eight-line plant traffic was 1.26592 Gbps.

Since the assignment does not specify AGV command traffic, the Task 1 robot-controller pattern of 200-byte commands every 2 ms is used as an explicit estimation assumption.

Estimated traffic for 50 AGVs = 40 Mbps.

Revised estimated plant traffic = **1.30592 Gbps**.

This requires additional backbone capacity and traffic prioritisation.

## B. Test of the Original Design
For a 1.2 km route at 2 m/s, one AGV takes 10 minutes to complete the trip.

| Technology | Handover count | Interruption per handover | Total interruption |
|---|---:|---:|---:|
| Wi-Fi | 39 | 150 ms | 5.85 seconds |
| Private 5G | 3 | 20 ms | 60 ms |

The required command deadline is 10 ms. Both handover times exceed this deadline. Private 5G reduces interruption considerably but requires further optimisation to meet the command requirement.

## C. Adaptation / Modified Design
The original design is modified as follows:

- Shielded Cat6A Ethernet for fixed robot controllers.
- Private 5G with URLLC-oriented configuration for AGVs.
- Overlapping coverage and make-before-break handover where supported.
- Wi-Fi 6 for office devices.
- Wired Ethernet/fibre and local recording for CCTV.
- Fibre backbone with redundant 10 Gbps or higher capacity.
- QoS, suitable error protection and local fail-safe control for critical commands.

## D. Evidence-Based Defence
The modified design is recommended because it retains the reliability and capacity of the original wired network while introducing mobility support for AGVs.

The estimated traffic increases from 1.26592 Gbps to 1.30592 Gbps per plant. For five plants with the same AGV population, the estimated aggregate becomes 6.5296 Gbps.

Private 5G reduces handover interruption compared with Wi-Fi, but its stated 20 ms handover still exceeds the 10 ms command deadline. Therefore, additional latency optimisation, redundancy and safety mechanisms are necessary.

## Conclusion
The original network should be modified rather than completely replaced. A hybrid architecture using shielded Ethernet, private 5G, Wi-Fi 6 and fibre provides a better balance of reliability, mobility, scalability and performance.

**Note:** AGV traffic figures are estimates based on the Task 1 robot-controller pattern because the assignment does not provide a separate AGV command rate.