# Task 5 – Detailed Calculations

## 1. Given Data

| Parameter | Value |
|---|---:|
| AGV speed | 2 m/s |
| Route length | 1.2 km = 1,200 m |
| Wi-Fi access point spacing | 30 m |
| Wi-Fi handover time | 150 ms |
| Private 5G cell coverage | 300 m |
| 5G handover time | 20 ms |
| Command deadline | 10 ms |

## 2. AGV Travel Time

Formula:

Travel time = Distance / Speed

Substituting:

= 1,200 / 2

= **600 seconds = 10 minutes**

## 3. Wi-Fi Handover Calculation

Number of coverage areas:

= Route length / Access point spacing

= 1,200 / 30

= 40 access point coverage areas

Number of handovers:

= 40 − 1

= **39 handovers**

Total handover interruption:

= Number of handovers × Handover time

= 39 × 150 ms

= 5,850 ms

= **5.85 seconds**

Comparison with command deadline:

= 150 / 10

= **15 times the deadline per handover**

## 4. Private 5G Handover Calculation

Number of coverage areas:

= Route length / Cell coverage

= 1,200 / 300

= 4 cell coverage areas

Number of handovers:

= 4 − 1

= **3 handovers**

Total handover interruption:

= Number of handovers × Handover time

= 3 × 20 ms

= 60 ms

= **0.06 seconds**

Comparison with command deadline:

= 20 / 10

= **2 times the deadline per handover**

## 5. Comparison of Total Interruption

| Parameter | Wi-Fi | Private 5G |
|---|---:|---:|
| Coverage areas | 40 | 4 |
| Handover count | 39 | 3 |
| Handover time | 150 ms | 20 ms |
| Total interruption | 5,850 ms | 60 ms |

Reduction in interruption:

= (5,850 − 60) / 5,850 × 100

= **98.97%**

Private 5G reduces the calculated total handover interruption by approximately 98.97% compared with Wi-Fi.

## 6. LoRaWAN Sensor Capacity Calculation

Given:

- Number of sensors = 600
- Data per sensor = 50 bytes/second
- Gateway capacity = 5 kbps

Data rate per sensor:

= 50 × 8

= **400 bits/second**

Total sensor data rate:

= 600 × 400

= 240,000 bits/second

= **240 kbps**

Gateway capacity:

= 5 kbps = 5,000 bits/second

Capacity ratio:

= 240,000 / 5,000

= **48**

Therefore, the sensors require 48 times the stated gateway capacity.

Maximum theoretical sensor count:

= 5,000 / 400

= 12.5

Therefore, approximately **12 sensors** can be supported under this simplified calculation, before accounting for protocol overhead and other LoRaWAN limitations.

## 7. Final Inference

Private 5G provides significantly lower total handover interruption than Wi-Fi in the given scenario. However, its individual 20 ms handover time still exceeds the 10 ms command deadline. LoRaWAN's stated 5 kbps gateway capacity is also insufficient for all 600 sensors transmitting at the specified rate.