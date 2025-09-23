

for i in range(0, 10):
    print(i)

print("===="*8)

for j in range(0, 10, 2):
    if j == 6: continue
    print(j)
else:
    print("Loop finished without any break")

for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Loop finished without break")  # Won’t run


order_nos = [345, 31, 45, 65]

for order in order_nos:
    print(order)

for index, order in enumerate(order_nos):
    print(f"{index}: {order} - {order_nos[index]}")

count = 10

while count >= 0:
    print(count)
    count -= 1

names = ["Dhoni", "Watson", "Mathew Hayden"]
runs = [45, 56, 44]

# zip combines 2 lists
for index, (player, run) in enumerate(zip(names, runs), start=1):
    print(f"{index}. {player} scored {run} runs")


from random import randint

temp = 0

while temp < 100:
    print(f"current temp is: {temp}")
    temp = temp + randint(0, 15)
else:
    if temp >= 100: print(f"water is boiling at {temp} C")