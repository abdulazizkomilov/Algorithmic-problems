def is_power_to_binary(num: int) -> bool:
    bit_count = 0
    while num != 0:
        bit_count += num & 1
        num >>= 1
    return bit_count == 1
