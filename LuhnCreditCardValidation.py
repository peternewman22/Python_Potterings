"""
Implementing the Luhn algorithm to check valid credit card numbers
https://en.wikipedia.org/wiki/Luhn_algorithm

A python implementation is already listed on the Wikipedia site, but I want to do it myself.

The formula verifies a number against its included check digit, which is usually appended to a partial account number to generate the full account number. This number must pass the following test:

1. From the rightmost digit (excluding the check digit) and moving left, double the value of every second digit. The check digit is neither doubled nor included in this calculation; the first digit doubled is the digit located immediately left of the check digit. If the result of this doubling operation is greater than 9 (e.g., 8 × 2 = 16), then add the digits of the result (e.g., 16: 1 + 6 = 7, 18: 1 + 8 = 9) or, alternatively, the same final result can be found by subtracting 9 from that result (e.g., 16: 16 − 9 = 7, 18: 18 − 9 = 9).

2. Take the sum of all the digits (including the check digit).

3. If the total modulo 10 is equal to 0 (if the total ends in zero) then the number is valid according to the Luhn formula; otherwise it is not valid.

"""

example_acc = "79927398713"

def checkLuhn(credit_card_number: str) -> bool:

    to_check = list(reversed(list(credit_card_number)))
    total = 0
    for i in range(len(to_check)):
        x = int(to_check[i])
        # print(f"checking {x}...")
        if i%2 == 1:
            x *= 2
            if x > 9:
                x -= 9
            # print(f"\tDoubling... x = {x}")
        total += x
        # print(f"\ttotal is now {total}")

    return total%10 == 0

to_test = [
    "79927398710",
    "79927398711",
    "79927398712",
    "79927398713",
    "79927398714",
    "79927398715",
    "79927398716",
    "79927398717",
    "79927398718",
    "79927398719"
]

for eachNumber in to_test:
    print(checkLuhn(eachNumber))
