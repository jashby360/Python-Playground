def isPrime(number):
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            # If true, number is not prime
            return False  # number is not a prime
        divisor += 1
    return True  # number is prime


def main():
    count = 0  # Count the number of prime numbers
    number = 2  # A number to be tested for primeness
    # Repeatedly find prime numbers
    while number <= 10000:
        # Print the prime number and increase the count
        if isPrime(number):
            count += 1
            print(number, end=(" " if count < 10 else "\n"))
        if count == 10:
            # Print the number and advance to the new line
            print()
            count = 0
        # Check if the next number is prime
        number += 1

main()
