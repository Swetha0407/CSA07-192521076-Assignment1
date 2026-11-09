# Task 5 – Wi-Fi 6 or 5G for Moving Equipment?

## 1. Objective

To compare Wi-Fi 6 and private 5G for moving AGVs, calculate handover interruptions, identify suitable 5G service types, and evaluate alternative wireless technologies for plant communication.

## 2. Handover Calculation

Given:
- AGV speed = 2 m/s
- Route length = 1.2 km = 1,200 m
- Wi-Fi access point spacing = 30 m
- Wi-Fi handover time = 150 ms
- Private 5G cell coverage = 300 m
- 5G handover time = 20 ms
- Command deadline = 10 ms

Assuming the AGV starts inside the first coverage area:

### Wi-Fi

Handover count = (1,200 / 30) − 1 = **39**

Total interruption = 39 × 150 = **5,850 ms = 5.85 seconds**

### Private 5G

Handover count = (1,200 / 300) − 1 = **3**

Total interruption = 3 × 20 = **60 ms = 0.06 seconds**

| Parameter | Wi-Fi | Private 5G |
|---|---:|---:|
| Handover count | 39 | 3 |
| Handover time | 150 ms | 20 ms |
| Total interruption | 5,850 ms | 60 ms |

Private 5G significantly reduces handover interruption. However, its individual 20 ms handover time is still greater than the 10 ms command deadline, so further validation and suitable mobility management are necessary.

## 3. 5G Service Type Selection

| Device | 5G Service Type | Reason |
|---|---|---|
| AGVs and robot controllers | URLLC | Require reliable, low-latency command delivery. |
| CCTV cameras | eMBB | Require high data rates for continuous video. |
| Sensors | mMTC | Supports a large number of low-data-rate connected devices. |

## 4. Alternative Wireless Technologies

| Technology | Suitable Use | Reason |
|---|---|---|
| Bluetooth | Nearby maintenance devices and peripherals | Short-range, low-power communication. |
| Zigbee | Low-rate environmental sensors | Low-power communication and mesh networking. |
| LoRa | Remote, non-critical monitoring | Long range and low power consumption. |

These technologies can complement Wi-Fi and 5G depending on the application's range, data rate and power requirements.

## 5. Wi-Fi 6 with Fast Roaming (802.11r)

IEEE 802.11r reduces roaming authentication delays between Wi-Fi access points.

The normal Wi-Fi handover time is 150 ms, which is 15 times the 10 ms command deadline.

Although fast roaming can reduce interruption, it cannot be assumed to guarantee the deadline without practical measurements.

Remaining risks include interference, congestion, packet loss, jitter, roaming delays and coverage gaps.

Therefore, Wi-Fi 6 with fast roaming is more suitable for less critical mobile devices than for commands requiring guaranteed 10 ms delivery.

## 6. LoRaWAN Capacity Analysis

Each sensor sends 50 bytes per second.

Data rate per sensor = 50 × 8 = 400 bits/sec.

For 600 sensors:

Total data rate = 600 × 400 = 240,000 bits/sec = **240 kbps**.

Given gateway capacity = 5 kbps.

Required capacity / available capacity = 240 / 5 = **48 times**.

Maximum theoretical number of sensors:

5,000 / 400 = 12.5, approximately **12 sensors**.

Therefore, all 600 sensors cannot fit within one gateway's approximate 5 kbps capacity at the given reporting rate. LoRaWAN is suitable only for a limited subset of low-rate, non-critical sensors under these assumptions.

## Detailed Calculation Sheet

The complete step-by-step calculations for AGV travel time, handover interruptions, deadline comparison and LoRaWAN capacity are available in [calculations.md](calculations.md).

## 7. Result

Wi-Fi and private 5G handover interruptions were calculated and compared. Private 5G provides significantly lower interruption, but its stated handover time still exceeds the 10 ms command deadline. Suitable 5G service types and alternative wireless technologies were identified. The LoRaWAN capacity calculation showed that one 5 kbps gateway cannot support all 600 sensors at the specified reporting rate.