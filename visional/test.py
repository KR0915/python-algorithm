import sys

def number_to_words(n):
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    if n < 0 or n > 99999:
        return "Number out of range"
    if 0 <= n < 10:
        return ones[n]
    elif 10 <= n < 20:
        return teens[n - 10]
    elif 20 <= n < 100:
        return tens[n // 10] + (" " + ones[n % 10] if n % 10 != 0 else "")
    elif 100 <= n < 1000:
        return ones[n // 100] + " Hundred" + (" " + number_to_words(n % 100).lower() if n % 100 != 0 else "")
    elif 1000 <= n < 100000:
        return number_to_words(n // 1000) + " Thousand" + (" " + number_to_words(n % 1000).lower() if n % 1000 != 0 else "")

def decimal_to_words(number_str):
    integer_part, decimal_part = number_str.split(".")
    integer_words = number_to_words(int(integer_part))
    decimal_words = " ".join(number_to_words(int(digit)).lower() for digit in decimal_part)
    return f"{integer_words} point {decimal_words}"

def main(lines):
    input_str = lines[0]

    if "." in input_str:
        print(decimal_to_words(input_str))
    else:
        n = int(input_str)
        print(number_to_words(n))

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)