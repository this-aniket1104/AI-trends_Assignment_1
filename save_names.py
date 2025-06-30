with open("names.txt", "w") as file:
    for i in range(5):
        name = input(f"Enter name {i+1}: ")
        file.write(name + "\n")
print("Names saved to names.txt")