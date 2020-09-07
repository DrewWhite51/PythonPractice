# Only allows Drew, and the password swordfish to access
while True:
    print("Who are you?")
    name = input(" ")
    if name != "Drew":
        continue
    print("Hello, Drew. What is the password? (It is a fish.)")
    password = input(" ")
    if password == "swordfish":
        break
print("Access granted")