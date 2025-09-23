name = input("What is your name ?  ")
age = int(input("What is your age ? "))
day = input("Which day of the week ? ").lower()
student = input("Are you a student ? (yes/no) ? ")

is_student = False

if student == "yes":
    is_student = True


BASE_PRICE = final_price = 200

if age < 12:
    final_price = BASE_PRICE / 2
elif age >= 60:
    final_price = BASE_PRICE - BASE_PRICE * 0.3
else:
    final_price = BASE_PRICE

print(f"Calculating final price after age: {final_price}")

if day == "wednesday" and not final_price < 50:
    final_price = final_price - final_price * 0.2

print(f"Calculating final price after day {final_price}")

if is_student and not final_price < 50:
    final_price = final_price - 50

print(f"Calculating final price after student {final_price}")

print(f"Final Price: {final_price}")
