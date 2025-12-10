from fractions import Fraction
from num2words import num2words

PADDING = 7


def text_to_fraction_unicode(input_text):
    number_string = ""

    for char in input_text:
        val = ord(char)
        number_string += f"{val:0{PADDING}d}"

    decimal_string = "0." + number_string
    exact_fraction = Fraction(decimal_string)

    return exact_fraction.numerator, exact_fraction.denominator, decimal_string


def fraction_to_text_unicode(numerator, denominator):
    digits = ""
    remainder = numerator

    while remainder != 0:
        remainder *= 10
        digit = remainder // denominator
        remainder %= denominator
        digits += str(digit)

    while len(digits) % PADDING != 0:
        digits += "0"

    result_text = ""
    for i in range(0, len(digits), PADDING):
        chunk = digits[i : i + PADDING]
        val = int(chunk)

        try:
            result_text += chr(val)
        except ValueError:
            result_text += "?"

    return result_text


complex_text = "Hi 🤖! (こんにちは)"

print(f"Original: {complex_text}")
n, d, f = text_to_fraction_unicode(complex_text)
print(f"Fraction: {n}\n          {'-' * 10}\n          {d}")

print(f"Numerator in words: {num2words(n)}")
print(f"Denominator in words: {num2words(d)}")

print(f"Decimal: {f}")
print(len(f.encode("utf-8")))
print(len(complex_text.encode("utf-8")))
restored = fraction_to_text_unicode(n, d)
print(f"Restored: {restored}")

if complex_text == restored:
    print("\nSUCCESS: The reconstruction is perfect.")
else:
    print("\nFAILURE: Data was lost.")
