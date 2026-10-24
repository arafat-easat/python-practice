# while True:
#     n = input("Please enter a positive number (0 to exit): ")
#     n = int(n)
#     if n < 0:
#         print("We only allow postive number.please try again")
#         continue
#     if n == 0:
#         break
#     print("square of", n, "is", n * n)


terminate = False
while not terminate:
    number1 = int(input("Please enter a number:"))
    number2 = int(input("Please enter another number:"))

    while True:
        operation = input("please enter add/sub or quit to exit:")
        if operation == "quit":
            terminate = True
            break
        if operation not in ["add", "sub"]:
            print("Unkknown operation!")
            continue
        if operation == "add":
            print("Result is:", number1 + number2)
            break
        if operation == "sub":
            print("Result is:", number1 - number2)
            break
