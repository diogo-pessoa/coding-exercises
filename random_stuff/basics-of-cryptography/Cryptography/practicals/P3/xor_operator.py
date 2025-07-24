value_a = "f89aa71b1d"
value_b = "0271bc8a89"
value_c = "8bb2dea901"

bytes_a = bytes.fromhex(value_a)
bytes_b = bytes.fromhex(value_b)
bytes_c = bytes.fromhex(value_c)

## Commutativity

# A XOR B
output_1 = bytearray()
for (x, y) in zip(bytes_a, bytes_b):
    output_1.append(x ^ y)

print(output_1.hex())

# B XOR A
output_2 = bytearray()
for (x, y) in zip(bytes_b, bytes_a):
    output_2.append(x ^ y)

print(output_2.hex())

## Associativity

# A XOR (B XOR C) = (A XOR B) XOR C
# Addition equivalent: 1 + (2 + 3) = (1 + 2) + 3

output_3 = bytearray()
for (x, y) in zip(bytes_b, bytes_c):
    output_3.append(x ^ y)

output_4 = bytearray()
for (x, y) in zip(bytes_a, output_3):
    output_4.append(x ^ y)

print(output_4.hex())

output_5 = bytearray()
for (x, y) in zip(output_1, bytes_c):
    output_5.append(x ^ y)

print(output_5.hex())

# Identity

value_zero = "0000000000"
bytes_zero = bytes.fromhex(value_zero)

output_6 = bytearray()
for (x, y) in zip(bytes_a, bytes_zero):
    output_6.append(x ^ y)

print(output_6.hex())

# Self-Inverse

output_7 = bytearray()
for (x, y) in zip(bytes_c, bytes_c):
    output_7.append(x ^ y)

print(output_7.hex())
