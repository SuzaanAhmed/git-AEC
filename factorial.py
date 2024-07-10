def main():
    factorial=int(input("Enter number: "))
    print(f"The factorial of {factorial} = {factorial(factorial)}")

def factorial(fact):
    if fact == 0:
        return 1
    else:
        return factorial(fact-1)*fact
    
if __name__ == "__main__":
    main()