def decimal_to_binary_recursive(decimal):
    if decimal == 0:
        return "0b0"
    else:
        return decimal_to_binary_recursive(decimal // 2) + str(decimal % 2)