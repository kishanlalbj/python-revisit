# Polymorphism = "many forms"
# Same method name, different behaviour depending on the object calling it.
# Senior tip: You call the same method on different objects — each object does it its own way.

print("=" * 40)
print("1. Method Overriding (Runtime Polymorphism)")
print("=" * 40)

# The parent defines WHAT should happen.
# Each child decides HOW it happens.

class Notification:
    def send(self, message):
        print(f"Sending: {message}")

class EmailNotification(Notification):
    def send(self, message):
        print(f"[EMAIL]  >> {message}")

class SMSNotification(Notification):
    def send(self, message):
        print(f"[SMS]    >> {message}")

class PushNotification(Notification):
    def send(self, message):
        print(f"[PUSH]   >> {message}")


# The real power: you don't need to know WHICH notification type it is.
# You just call .send() and Python figures out the rest.
notifications = [
    EmailNotification(),
    SMSNotification(),
    PushNotification(),
]

for notif in notifications:
    notif.send("Your OTP is 4892")


print("\n" + "=" * 40)
print("2. Duck Typing (Python's flavour of polymorphism)")
print("=" * 40)

# Senior tip: Python doesn't check the TYPE of the object.
# It only checks: "does this object have the method I'm calling?"
# "If it walks like a duck and quacks like a duck — it's a duck."

class PDFReport:
    def export(self):
        print("Exporting as PDF...")

class ExcelReport:
    def export(self):
        print("Exporting as Excel...")

class JSONReport:
    def export(self):
        print("Exporting as JSON...")

# No inheritance needed. No shared base class. Just a shared method name.
def export_all(reports):
    for report in reports:
        report.export()  # works for ANY object that has .export()

export_all([PDFReport(), ExcelReport(), JSONReport()])


print("\n" + "=" * 40)
print("3. Method Overloading (Python style)")
print("=" * 40)

# Senior tip: Python doesn't support true overloading (same method, different params).
# Instead, use default arguments or *args to handle multiple call signatures.

class Calculator:
    def add(self, a, b, c=0):  # c is optional
        return a + b + c

calc = Calculator()
print(calc.add(2, 3))       # 5
print(calc.add(2, 3, 4))    # 9

# *args: accept any number of arguments — fully flexible
class FlexCalculator:
    def add(self, *numbers):    # 2 args, 3 args, 10 args — all work
        return sum(numbers)

flex = FlexCalculator()
print(flex.add(2, 3))           # 5
print(flex.add(2, 3, 4))        # 9
print(flex.add(1, 2, 3, 4, 5))  # 15


print("\n" + "=" * 40)
print("4. Polymorphism with built-in functions")
print("=" * 40)

# Senior tip: Python's built-ins already use polymorphism.
# len(), str(), + all behave differently based on the type.

print(len("hello"))       # works on string
print(len([1, 2, 3]))     # works on list
print(len({"a": 1}))      # works on dict

print(1 + 2)              # addition
print("Hello" + " World") # concatenation — same operator, different behaviour
