
lang = "de"

def greet(name):
    # local scope, not accessible outside
    lang = "en"

    if lang == "en": return f"Hello, {name}"
    elif lang == "de": return f"Hallo, {name}"
    else: return "Vanakkam da, {name}"


print(greet("John"))

def greet_lang():
    lang = "ta"
    def greet():
        lang = "te"
        print("Inner ", lang)
    greet()
    print("outer ", lang)


greet_lang()


# We can use keyword nonlocal to access the outer scope variables.

def greet_lang2():
    print("============== Non Local ============")
    lang = "ta"
    def greet():
        nonlocal lang
        print(lang)
        lang = "gibbrish"
    greet()
    print("outer ", lang)


greet_lang2()