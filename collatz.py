def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number //2
        
    elif number % 2 == 1:
        n = 3 * number + 1
        print(n)
        return n


try:
    number = int(input("Enter number: \n"))
    while True:
        while number != 1:
            number = collatz(number)
except ValueError:
    print("Please enter integer value")