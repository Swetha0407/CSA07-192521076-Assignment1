# Task 9 – Detailed Window Size and ARQ Calculations

## 1. Given Data

| Parameter | Value |
|---|---:|
| Head-office distance | 400 km = 400,000 m |
| Link rate | 1 Gbps = 10⁹ bps |
| Frame size | 1,500 bytes = 12,000 bits |
| Propagation speed | 2 × 10⁸ m/s |

## 2. Transmission Time

Formula:

Transmission time = Frame size / Link rate

= 12,000 / 10⁹

= 0.000012 seconds

= **12 microseconds**.

## 3. Propagation Time

Propagation time = Distance / Propagation speed

= 400,000 / (2 × 10⁸)

= 0.002 seconds

= **2 ms**.

## 4. Ratio a

a = Propagation time / Transmission time

= 0.002 / 0.000012

= **166.67**.

## 5. Stop-and-Wait Utilisation

Formula:

U = 1 / (1 + 2a)

= 1 / (1 + 2 × 166.67)

= **0.299%, approximately 0.3%**.

Throughput:

= 0.002991 × 1,000 Mbps

= **2.99 Mbps approximately**.

## 6. Minimum Sliding Window

For full utilisation:

W ≥ 1 + 2a

= 1 + 2 × 166.67

= 334.34

Therefore, the minimum whole-number window is:

**W = 335 frames**.

## 7. Sequence Number Bits

### Go-Back-N

W ≤ 2ᵏ − 1.

For W = 335:

- 8 bits provide a maximum window of 255.
- 9 bits provide a maximum window of 511.

Required sequence-number bits = **9 bits**.

### Selective Repeat

W ≤ 2ᵏ⁻¹.

For W = 335:

- 9 bits provide a maximum window of 256.
- 10 bits provide a maximum window of 512.

Required sequence-number bits = **10 bits**.

## 8. Go-Back-N vs Selective Repeat

Go-Back-N retransmits the lost frame and subsequent unacknowledged frames in the window.

Selective Repeat retransmits only the missing frame and buffers correctly received out-of-order frames.

Selective Repeat reduces unnecessary retransmissions but requires more receiver buffer space and implementation complexity.

## 9. HDLC and PPP Frame Boundaries

Both HDLC and PPP use the flag sequence:

**01111110**

The flag marks the beginning and end of a frame.

Bit stuffing inserts a 0 after five consecutive 1s in the data to prevent accidental appearance of the flag pattern. The receiver removes the inserted bit.

## 10. Satellite Link Calculation

Given:

- Distance = 36,000 km = 36,000,000 m
- Rate = 10 Mbps
- Frame size = 12,000 bits
- Propagation speed = 2 × 10⁸ m/s

Transmission time:

= 12,000 / 10⁷

= **0.0012 seconds**.

Propagation time:

= 36,000,000 / (2 × 10⁸)

= **0.18 seconds**.

Ratio:

a = 0.18 / 0.0012 = **150**.

Minimum window:

W ≥ 1 + 2 × 150

= **301 frames**.

## 11. Selective Repeat with Window 64

For the head-office link:

U = 64 / (1 + 2 × 166.67)

= **19.14% approximately**.

Throughput:

= 0.1914 × 1,000 Mbps

= **191.4 Mbps approximately**.

Receiver window buffer:

= 64 × 1,500

= **96,000 bytes**.

If one frame at the beginning of the window is lost, the following 63 frames can arrive out of order:

= 63 × 1,500

= **94,500 bytes**.

## 12. Result

Transmission and propagation times were calculated for the head-office link. Stop-and-Wait achieves approximately 0.3% utilisation, while a sliding window of 335 frames is required for full utilisation under the given model. Go-Back-N requires 9 sequence-number bits and Selective Repeat requires 10 bits. The satellite link requires a window of 301 frames for full utilisation. Selective Repeat with a window of 64 achieves approximately 19.14% utilisation on the head-office link.