
def main_welcome(func):
    print("Welomee")
    def wrapper():
        func()
    return wrapper


@main_welcome
def read_again():
    print("Read again...")


read_again()