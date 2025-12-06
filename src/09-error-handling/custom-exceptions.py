class MuskondeOoguError(Exception):
    pass


def calculate_something(amount):
    try:
        if(amount <= 0): raise MuskondeOoguError("Oogu Bewarsi'nan maga")
    except Exception as e:
        print(e)
    else:
        print(amount * 10)


calculate_something(0)
    