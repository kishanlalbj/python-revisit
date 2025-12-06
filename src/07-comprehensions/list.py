list = [
    "Tea",
    "Iced Tea",
    "Ginger Tea",
    "Iced Ginger Tea"
]

iced_tea = [tea for tea in list if len(tea) > 10]

print(iced_tea)
