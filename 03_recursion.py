def countdown(i):
    print(i)
    # base case: if i is less than or equal to 0, stop the recursion
    if i <= 0:
        return
    # recursive case: if i is greater than 0, call the function again with i-1
    else:
        countdown(i - 1)


def greet(name):
    print("hello, " + name + "!")
    greet2(name)
    print("getting ready to say bye...")
    bye()


def greet2(name):
    print("how are you, " + name + "?")


def bye():
    print("ok bye!")


def fact(x):
    # base case: if x is 1, return 1
    if x == 1:
        return 1
    # recursive case: if x is greater than 1, return x multiplied by the factorial of x-1
    else:
        return x * fact(x - 1)


if __name__ == "__main__":
    countdown(5)
    greet("maggie")
    print(fact(3))
