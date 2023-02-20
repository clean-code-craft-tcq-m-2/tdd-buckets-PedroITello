min_value = 0
max_value = 0


def read_10_bit_input(data, min, max):
    if (data != 511):
        voltage_range(min, max)
        result = convert_10_bit_to_amps(data)
        print(str(result) + " Amps")
        return result
    else:
        print("NOT CURRENT")
        return "NOT CURRENT"


def convert_10_bit_to_amps(data):
    if (data < 511):
        return min_value
    return max_value


def voltage_range(min, max):
    global min_value
    global max_value
    min_value = min
    max_value = max
