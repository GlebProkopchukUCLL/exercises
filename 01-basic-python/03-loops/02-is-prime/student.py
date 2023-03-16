# Write your code here
def is_prime(n):
    return False if n >= 0 and n <= 1 else all(n % i != 0 for i in range(2, n))