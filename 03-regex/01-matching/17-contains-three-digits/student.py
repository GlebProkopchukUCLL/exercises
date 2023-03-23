import re
# Write your code here
def contains_three_digits(string):
    return re.fullmatch('.*\d.*\d.*\d.*', string)