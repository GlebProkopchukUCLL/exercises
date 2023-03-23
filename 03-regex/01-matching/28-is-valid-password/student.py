# Write your code here
import re
def is_valid_password(string):
    return re.search(r'[\d+a-z+A-Z+[+-*/.@]+^(.)\1\1,^.{4}]{12,}', string)