

def divide(a, b):
    try:
        if(b == 0): raise ZeroDivisionError("It will be infinite")
        result = a / b       
    except ZeroDivisionError as e:
        print("Cannot be divied by 0")
        print(e)
        print("Bewarsi nan maga, Morskonde oogu..")
    else:
        print(result)
    finally:
        print("Thank you for using our services! :)")


divide(4, 3)

divide(2, 2)

divide(1, 0)