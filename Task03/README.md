# Task 3 – Read a Captured Frame Layer by Layer

## 1. Objective
To analyse an Ethernet frame layer by layer, identify its OSI layers and PDUs, calculate packet overhead, and demonstrate encapsulation and decapsulation using Python.

## 2. Captured Frame Analysis

| Protocol | OSI Layer | PDU |
|---|---|---|
| Ethernet II | Layer 2 – Data Link | Frame |
| IPv4 | Layer 3 – Network | Packet |
| TCP | Layer 4 – Transport | Segment |
| Modbus Data | Application data | Data |

The sender uses encapsulation to add protocol headers and trailers. The receiver performs decapsulation to recover the original message.

## 3. Router Count

Initial TTL = 64  
Captured TTL = 61

Routers crossed = 64 − 61 = **3 routers**.

## 4. Frame Size and Overhead

For the 12-byte Modbus command:

- Ethernet header = 14 bytes
- IPv4 header = 20 bytes
- TCP header = 20 bytes
- Data = 12 bytes
- FCS = 4 bytes

Total = **70 bytes**

Overhead = 14 + 20 + 20 + 4 = 58 bytes.

Overhead percentage = (58 / 70) × 100 = **82.86%**.

For a 1,400-byte camera message:

Total = 1,400 + 28 = 1,428 bytes in the simplified Python model.

Overhead percentage = (28 / 1,428) × 100 = **1.96%**.

This demonstrates that small commands have a higher overhead percentage than large messages.

## 5. Fault-to-Layer Mapping

| Fault | OSI Layer |
|---|---|
| Incorrect MAC address | Layer 2 – Data Link |
| TTL reaches zero | Layer 3 – Network |
| Destination port closed | Layer 4 – Transport |

## 6. TCP/IP and OSI Mapping

| TCP/IP Model | OSI Layers |
|---|---|
| Application | Layers 5, 6 and 7 |
| Transport | Layer 4 |
| Internet | Layer 3 |
| Network Access | Layers 1 and 2 |

## 7. Python Encapsulation Program

The Python program demonstrates how HTTP, TCP, IP and Ethernet tags are added to a message at the sender and removed at the receiver.

**Execution:** `python Task03/encapsulation.py`

The program successfully wrapped the message, displayed the PDU size at each layer, and recovered the original message through decapsulation.

## 8. Alternative Concept Analysis

Using direct industrial Ethernet with EtherType 0x8892 removes the 20-byte IPv4 header and 20-byte TCP header.

Bytes saved per command = **40 bytes**.

On a 100 Mbps link, this represents a theoretical saving equivalent to 312,500 commands per second.

However, removing IP and TCP reduces compatibility with standard IP routing and applications. The choice depends on the plant's real-time requirements and integration needs.

## 9. Result

The captured frame was analysed successfully. Router count, protocol overhead, OSI layer responsibilities and TCP/IP mapping were determined. The Python program demonstrated encapsulation and decapsulation, and the alternative industrial Ethernet approach was evaluated.