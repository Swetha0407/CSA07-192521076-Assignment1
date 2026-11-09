# Task 10 – Detailed Delay Analysis Calculations

## 1. Given Traceroute

| Hop | IP Address | Probe 1 | Probe 2 | Probe 3 |
|---|---|---:|---:|---:|
| 1 | 10.10.1.1 | 0.6 ms | 0.5 ms | 0.6 ms |
| 2 | 100.64.0.1 | 3.1 ms | 2.9 ms | 3.4 ms |
| 3 | 172.31.4.9 | 4.0 ms | 38.2 ms | 4.2 ms |
| 4 | 103.21.8.17 | 11.8 ms | 11.5 ms | 12.1 ms |
| 5 | No response | * | * | * |
| 6 | 10.200.0.10 | 12.6 ms | 12.4 ms | 12.9 ms |

## 2. Fibre Propagation Delay

Given:

- Distance = 400 km = 400,000 m
- Propagation speed = 2 × 10⁸ m/s

One-way propagation delay:

T = Distance / Speed

= 400,000 / (2 × 10⁸)

= 0.002 seconds

= **2 ms**.

Round-trip propagation delay:

= 2 × 2

= **4 ms**.

Average final-hop response time:

= (12.6 + 12.4 + 12.9) / 3

= **12.63 ms**.

Estimated percentage explained by fibre propagation:

= (4 / 12.63) × 100

= **31.67% approximately**.

This assumes a roughly symmetric round trip. Actual traceroute RTT includes router processing, queueing and other network delays.

## 3. Hop 3 Delay Spike

Hop 3 records 4.0 ms, 38.2 ms and 4.2 ms.

The second measurement is significantly higher than the other two. Possible causes include temporary congestion, queueing, router processing load or delayed ICMP response handling.

The spike does not automatically indicate a faulty router because subsequent measurements are normal.

Normal-response average:

= (4.0 + 4.2) / 2

= **4.1 ms**.

## 4. Hop 5 Non-response

Hop 5 displays three asterisks, indicating that no response was received before the timeout.

Possible causes include ICMP filtering, rate limiting or routers configured not to respond to traceroute probes.

Since hop 6 responds successfully, the missing response does not prove that the network is broken.

## 5. Hop Delay Comparison

| Hop | Average RTT |
|---|---:|
| 1 | 0.57 ms |
| 2 | 3.13 ms |
| 3 | 15.47 ms |
| 4 | 11.80 ms |
| 6 | 12.63 ms |

Hop 3's average is affected by its isolated high reading. Considering its normal measurements, the increase from hop 3 to hop 4 is:

11.8 − 4.1 = **7.7 ms**.

Hop 4 is associated with the largest consistent increase in response time. These differences are approximate because traceroute reports round-trip probe times rather than individual one-way link delays.

## 6. SNMP, NetFlow and Diagnostic Tests

SNMP monitors interface statistics such as traffic, errors and discarded packets.

NetFlow records traffic flows and helps identify bandwidth-heavy devices and applications.

Ping measures reachability and round-trip time. Traceroute identifies the path and response times at successive hops.

Continuous monitoring using SNMP and NetFlow provides better visibility into recurring issues, while ping and traceroute are useful for targeted troubleshooting.

## 7. Result

The expected one-way propagation delay for 400 km of fibre was calculated as 2 ms. The estimated round-trip propagation delay is 4 ms, approximately 31.67% of the final-hop average response time under a symmetric-path assumption.

The hop 3 spike was identified as a possible temporary delay, and hop 5's non-response was not treated as proof of a fault. Ping, traceroute and Wireshark were used to collect real network evidence.