# Write your code here
def last_digit(digit):
    return digit % 10

def remove_last_digit(digit):
    return digit // 10

def digit_sum(digit):
    sum = 0
    while digit > 0:
        sum += last_digit(digit)
        digit = remove_last_digit(digit)
    return sum