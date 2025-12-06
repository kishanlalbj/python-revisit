file = open("test.log", "w")

try:
    file.write("Testingggggggg")
except Exception as e:
    print(e)
finally:
    file.close()



with open("test2.log", "w") as file:
    file.write("Test")
