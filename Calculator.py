while True:
    print("Options:")
    print("Enter 'a' to add two nubbers")
    print("Enter 's' to subtract two nubbers")
    print("Enter 'm' to multiply two nubbers")
    print("Enter 'd' to divide two nubbers")
    print("Enter 'q' to end the program")
    user_input = input(": ")
    if user_input == "q":
        break
    elif user_input == "a":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 + num2)
    elif user_input == "s":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 - num2)
    elif user_input == "m":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 * num2)
    elif user_input == "d":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 / num2)
    else:
        print("Unnown input")
    print("The answer is: " + result)


