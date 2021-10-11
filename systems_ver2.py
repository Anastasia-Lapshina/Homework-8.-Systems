def systems(number, system):
    result = []
    while number >= 0:
        result.append(number % system)
        number = number // system
        if number == 0:
            break
    result.reverse()
    final = ''.join(map(str, result))
    return final


print("Enter a number you'd like to convert: ")
try:
    number = int(input())
except ValueError:
    print("Invalid data. Enter a natural number or zero")
    quit()
print('''Choose a system you want to convert your number into:
2 ← binary system
8 ← octal system''')
try:
    system = int(input())
except ValueError:
    print("Invalid data. Enter either 2 or 8")
else:
    if system == 2 and 0 <= number < 256:
        print("Your number in binary systems equals: ", systems(number, 2))
    elif system == 8:
        print("Your number in octal systems equals: ", systems(number, 8))
    elif system == 2 and (number < 0 or number > 255):
        print("Invalid data. Only numbers in range [0;255] can be converted into binary system")
        quit()
