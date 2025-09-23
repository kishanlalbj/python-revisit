favourite_chais = [
    "Masala Chai",
    "Green Tea",
    "Ginger Tea",
    "Ginger Tea",
    "Elachi Chai",
    "Black Tea"
]

unique_chai = {chai for chai in favourite_chais}

print(f"unique chais {unique_chai}")


recipes = {
    "masala_chai": ["ginger", "cardamom", "clove"],
    "elachi_chai": ["elaichi", "clove"],
    "ginger": ["ginger"],
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}


print(f"Uniqe spices", unique_spices)