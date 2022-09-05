# print(f"The __name__ of script_1.py is: {__name__}")


# if __name__ == '__main__':
#     print(f"The __name__ of script_1.py is: {__name__}.")


# if __name__ == "__main__":
#     print(f"Я работаю, как независимая программа с именем {__name__}.")
# else:
#     print(f"Я работаю, как импортированная программа с именем {__name__}.")

def say_hello(name=""):
    print(f"Hello, {name}!")


def set_age(age=20):
    print(f"My age: {age} years ago.")


def main():
    name = input("Enter your name: ")
    say_hello(name=name)
    set_age(age=45)
    print(f"Я работаю, как независимая программа с именем {__name__}.")


if __name__ == "__main__":
    main()
