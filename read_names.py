try:
    with open("names.txt", "r") as file:
        print("Stored Names:")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("names.txt not found. Please run save_names.py first.")