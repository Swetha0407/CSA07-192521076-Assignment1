# Task 11 – Network Design Calculations

## 1. Five-plant traffic requirement

Traffic for one plant = 1.26592 Gbps

Traffic for five plants:

1.26592 × 5 = 6.3296 Gbps

A 10 Gbps fibre backbone is recommended as a starting point, with sufficient capacity headroom and redundancy.

## 2. CCTV motion-triggered traffic

Revised traffic per plant = 536.32 Mbps

For five plants:

536.32 × 5 = 2681.6 Mbps = 2.6816 Gbps

Local CCTV recording and motion-triggered transmission significantly reduce backbone traffic.

## 3. Long-distance link calculation

Frame size = 1500 bytes = 12000 bits

Transmission rate = 1 Gbps

Transmission time:

Tt = 12000 / 10^9 = 12 microseconds

Propagation time:

Tp = 400000 / (2 × 10^8) = 2 ms

a = Tp / Tt = 166.67

Required window:

W ≥ 1 + 2a

W ≥ 334.34

Therefore, a minimum window of 335 frames is required for theoretical full utilisation.

## 4. Error-control justification

- CRC detects transmission errors in Ethernet frames.
- Hamming code can correct a single-bit error.
- FEC is useful where retransmission could violate a time deadline.
- TCP retransmission is suitable for reliable office and head-office data transfer.

## 5. Delay justification

Robot command deadline = 10 ms.

Wi-Fi handover = approximately 150 ms.

Private 5G handover = approximately 20 ms.

Both handover times exceed the 10 ms deadline. Therefore, critical robot control should use a deterministic wired connection wherever possible.