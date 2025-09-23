name = "Ultimate_Start_Ajith_Kumar"

print(type(name))

print(name[0])

print(f"Every second character {name[0:-1:2]}")
print(f"{name[::-1]}")



print(f"Swap variables")
main_lead = "Arjun"
side_lead = "Ajith"
print(f"main lead {main_lead}")
print(f"side_lead {side_lead}")

main_lead, side_lead = side_lead, main_lead

print("==============After Swapping===========")

print(f"main lead {main_lead}")
print(f"side_lead {side_lead}")