import tdd_buckets_constants as tddbc


def read_12_bit_input(data):
    if (data < 4094):
        conversion = convert_12_bit_to_amps(data)
        print(str(conversion) + " Amps")
        return conversion
    else:
        print("READING ERROR")
        return "ERROR"


def convert_12_bit_to_amps(data):
    conversion_value = data * 100 / tddbc.MAX_12_BIT_VALUE
    result = round(conversion_value / 10)
    return result
