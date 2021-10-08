def systems(number, system):
    result = []
    while number > 0:
        result.append(number % system)
        number = number // system
    result.reverse()
    final = ''.join(map(str, result))
    if system == 2:
        print(f"Your number in binary systems equals: {final}")
    elif system == 8:
        print(f"Your number in octal system equals: {final}")


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
    quit()
if (system == 2 and 0 <= number < 256) or system == 8:
    systems(number, system)
else:
    print("Invalid data. Enter an integer in range [0;255]")
    quit()
