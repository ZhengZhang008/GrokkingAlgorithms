def countdown(i):
    print(i)
    # base case
    if i <= 0:
        return
    # recursive case
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
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)


if __name__ == "__main__":
    countdown(5)
    greet("maggie")
    print(fact(3))
