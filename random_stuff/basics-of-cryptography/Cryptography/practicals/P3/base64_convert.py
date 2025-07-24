import base64

hex_str = "456163682068657861646563696D616C20646967697420726570726573656E747320666F75722062697473206F722061206E6962626C652E"

# Convert from hex string into a byte array

byte_array = bytes.fromhex(hex_str)

# Convert from the byte array into a Base64 string

base64_str = base64.b64encode(byte_array).decode("ascii")

print(base64_str)

