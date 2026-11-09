
"""CRC error detection for frames sent between two switches."""


def mod2_div(dividend, divisor):
    """Return the remainder of modulo-2 (XOR) division of two bit strings."""
    rem = list(dividend)
    for i in range(len(dividend) - len(divisor) + 1):
        # TODO 1: If the current leading bit rem[i] is 1, XOR the divisor into rem
        # starting at position i
        if rem[i] == "1":
            for j in range(len(divisor)):
                rem[i + j] = str(int(rem[i + j]) ^ int(divisor[j]))

    return "".join(rem[-(len(divisor) - 1):])


def encode(data, gen):
    crc = mod2_div(data + "0" * (len(gen) - 1), gen)
    return data + crc


def check(frame, gen):
    return set(mod2_div(frame, gen)) == {"0"}


GEN = "1011"  # x^3 + x + 1
frame = encode("1101011011", GEN)
print("transmitted:", frame)
print("no error   :", check(frame, GEN))

bad = frame[:4] + ("1" if frame[4] == "0" else "0") + frame[5:]
print("1-bit error:", check(bad, GEN))

burst = frame[:2] + "".join(
    "1" if b == "0" else "0" for b in frame[2:5]
) + frame[5:]
print("3-bit burst:", check(burst, GEN))

# Additional test: an undetectable error pattern
undetected = "0000000001011"
print("undetected pattern remainder:", mod2_div(undetected, GEN))
print("undetected error accepted  :", check(
    "".join(str(int(a) ^ int(b)) for a, b in zip(frame, undetected)),
    GEN
))
