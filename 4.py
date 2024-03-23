number = int(input())
if number // 10 == 1:
    print(number, "попугаев")
else:
    last_digit = number % 10
    if last_digit == 1:
        print(number, "попугай")
    elif 2 <= last_digit <= 4:
        print(number, "попугая")
    else:
        print(number, "попугаев")
