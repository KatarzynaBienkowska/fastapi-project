from sympy.ntheory.primetest import mr


def is_prime(number: int):
    maximum = 9223372036854775807
    if 1 < number < maximum:
        ps = [2, 3, 5, 7, 11, 13, 17, 19, 23]
        for i in range(9):
            if not mr(number, ps):
                return f"{number} is not a prime number"
        return f"{number} is a prime number"
    else:
        return f"Invalid number or your number is greater than {maximum}"
