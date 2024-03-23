def check_pin(pin):
    if len(pin) != 4 or not pin.isdigit():
        return "ERROR"
    if len(set(pin)) != 4:
        return "ERROR"

    birth_years = set(range(1900, 2051))
    if int(pin) in birth_years:
        return "ERROR"

    return "OK"

pin = input()

check = check_pin(pin)
print(check)