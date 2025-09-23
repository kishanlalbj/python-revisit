

age = 17

if age >= 18 and age < 21:
    print("You are eligible to vote, not to drink")
elif age >= 21 and age < 30:
    print("You can drink")
elif age >=30:
    print("You need to stop drinking")
else:
    print("You need to grow up")



# ternary operators

status = "adult" if age >= 18 else "minor"

marks = 85

grade = "A" if marks >= 90 else "B" if marks >=75 else "C"

# switch case 

day = input("What is the day today ?")

match day.lower():
    case "monday":
        print("Start of the week")
    case "friday":
        print("Almost weekend")
    case "saturday" | "sunday":
        print("Weekend !")
    case _:
        print("Regular weekday")



# := is called walrus operator. we also them in Go in different context.
value = 13

if remainder := value % 5:
    print(f"Remainde is {remainder}")
