def calculate_interest(amount):
    try:
        if(amount <= 0):
            raise ValueError("Value cannot be 0 or less than 0")
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
        print("Type npt matched")
    else: 
        print(amount * 7.8/100)



calculate_interest(1000)
calculate_interest(20000)
calculate_interest(0)
calculate_interest(-1)
calculate_interest("test")
