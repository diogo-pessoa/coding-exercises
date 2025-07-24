hex_str = "456163682068657861646563696D616C20646967697420726570726573656E747320666F75722062697473206F722061206E6962626C652E"

# Convert from hex string to array of bytes

byte_array = bytes.fromhex(hex_str)

# Convert from array of bytes to string (ASCII)

ascii_str = byte_array.decode("ascii")

print(ascii_str)
