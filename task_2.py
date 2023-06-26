def get_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def perform_fraction_operations(fraction1, fraction2):
    numerator1, denominator1 = map(int, fraction1.split('/'))
    numerator2, denominator2 = map(int, fraction2.split('/'))

    nok = (denominator1 * denominator2) // get_gcd(denominator1, denominator2)

    new_numerator1 = numerator1 * (nok // denominator1)
    new_numerator2 = numerator2 * (nok // denominator2)

    sum_numerator = new_numerator1 + new_numerator2
    product_numerator = numerator1 * numerator2

    nod_sum = get_gcd(sum_numerator, nok)
    nod_result = get_gcd(product_numerator, denominator1 * denominator2)

    sum_fraction = f"{sum_numerator // nod_sum}/{nok // nod_sum}"
    product_fraction = f"{product_numerator // nod_result}/{(denominator1 * denominator2) // nod_result}"

    return sum_fraction, product_fraction

# Пример использования
fraction1 = input("Введите первую дробь (в формате a/b): ")
fraction2 = input("Введите вторую дробь (в формате a/b): ")

sum_result, product_result = perform_fraction_operations(fraction1, fraction2)

print("Сумма дробей:", sum_result)
print("Произведение дробей:", product_result)