print("Sum of n numbers:")
a = int(input("Enter n: "))
sum = 0
for i in range(1, a+1):  # Start from 1 and go up to and including n
    sum += i
print(f"Sum of {a} numbers = {sum}")
