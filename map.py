# Function to check if a number is even
def is_even(number):
    return number % 2 == 0

# Example usage
num = 10
if is_even(num):
    print(f"{num} is even")
else:
    print(f"{num} is odd")
