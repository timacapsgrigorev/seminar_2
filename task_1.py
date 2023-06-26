def decimal_to_hex(decimal):
    if decimal == 0:
        return '0'

    hex_chars = "0123456789ABCDEF"
    hex_string = ""

    while decimal > 0:
        remainder = decimal % 16
        hex_string = hex_chars[remainder] + hex_string
        decimal = decimal // 16

    return hex_string


number = int(input("Введите целое число: "))
hexadecimal = decimal_to_hex(number)
print("Шестнадцатеричное представление:", hexadecimal)