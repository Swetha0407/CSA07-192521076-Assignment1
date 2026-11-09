# Task 7 – Detailed Error Detection Calculations

## 1. CRC Calculation

Given:

- Data = 1101011011
- Generator = 1011
- Generator polynomial = x³ + x + 1

Number of CRC bits = 4 − 1 = 3.

Append three zeros:

1101011011 → 1101011011000

Perform modulo-2 division using XOR operations.

The final remainder is:

**CRC = 100**

Transmitted frame:

1101011011 + 100 = **1101011011100**

## 2. Received Frame Verification

Received frame = 1101011011101

Generator = 1011

Modulo-2 division gives remainder = **001**.

Since the remainder is non-zero, the receiver rejects the frame.

## 3. Burst Error Detection

Generator degree = 3.

A CRC generator of degree 3 detects all burst errors of length up to 3 bits.

Therefore, the longest guaranteed detectable burst is **3 bits**.

An undetectable error pattern is 1011 because it is an exact multiple of the generator polynomial and produces remainder 000.

## 4. Two-Dimensional Parity

Using even parity, the selected data block is:

| | C1 | C2 | C3 | C4 | Row parity |
|---|---:|---:|---:|---:|---:|
| R1 | 1 | 0 | 1 | 1 | 1 |
| R2 | 0 | 1 | 1 | 0 | 0 |
| R3 | 1 | 1 | 0 | 0 | 0 |
| R4 | 0 | 0 | 1 | 1 | 0 |
| Column parity | 0 | 0 | 1 | 0 | 1 |

A four-bit rectangular error affecting R1C1, R1C2, R2C1 and R2C2 is undetected. Each affected row and column has two flipped bits, so all parity checks still pass.

## 5. Internet Checksum

Given hexadecimal words:

4500, 0073, 0000, 4000

Addition:

4500 + 0073 + 0000 + 4000 = 8573

One's complement:

FFFF − 8573 = **7A8C**

Internet checksum = **7A8C**.

## 6. CRC and Even-Parity Comparison

| Error pattern | Even parity | CRC-3 |
|---|---|---|
| 11 (two flipped bits) | Undetected | Detected |
| 1111 (four flipped bits) | Undetected | Detected |
| 11101 (four flipped bits) | Undetected | Undetected |

Even parity misses all even-numbered bit errors. CRC-3 detects all burst errors up to three bits, but can miss longer error patterns that are multiples of its generator polynomial.

## 7. Result

The CRC bits were calculated as 100, and the transmitted frame was obtained as 1101011011100. The received frame with remainder 001 was rejected. Two-dimensional parity and the Internet checksum were also calculated. The comparison showed that CRC-3 provides stronger error detection than a simple even-parity bit, although it cannot detect every possible error pattern.