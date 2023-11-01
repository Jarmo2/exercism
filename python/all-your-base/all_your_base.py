BASE_2 = 2
BASE_3 = 3
BASE_10 = 10

def rebase(input_base, digits, output_base):
    rev_digits = digits[::-1]
    if input_base < 2:
        raise ValueError("input base must be >= 2")

    if any(digit for digit in digits if digit > input_base):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    if output_base < 2:
        raise ValueError("output base must be >= 2")
    
    if output_base == BASE_10:
        result = 0
        for i, digit in enumerate(rev_digits):
            result += digit * input_base ** i
        return [int(part) for part in str(result)]

    if input_base == BASE_10 and output_base == BASE_2:
        return [int(element) for element in bin(*digits)[2:]]

    for digit in digits:
        if digit == 0:
            return [0]
        digits = []
        while digit:
            digits.append(int(digit % output_base))
            digit //= output_base
        return digits[::-1]

    # hexadecimel to trinary
    #rebase(16, [2, 10], 3), [1, 1, 2, 0])
print(rebase(16, [2, 10], 3))