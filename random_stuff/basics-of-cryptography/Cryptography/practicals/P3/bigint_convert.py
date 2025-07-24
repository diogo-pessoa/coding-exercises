big_int = 340729841873182715861397179830856685654259321469692096127599848700034616712989535822328482917313631271598534498956022105309715286325299982013279476538056591160110165234154673739790739055092222057941412390792396213095811103894699574920250324039897163263561

# Convert the big int into a byte array

size_in_bytes = (big_int.bit_length() + 7) // 8 # computes the length in bytes exactly

byte_array = big_int.to_bytes(size_in_bytes, "little")

# Convert the byte array into a string (ASCII)

ascii_str = byte_array.decode("ascii")

print(ascii_str)

