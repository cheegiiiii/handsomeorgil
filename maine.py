print("Hello world")

with open("data.txt", "r") as file:
    print(file.read())

print("kebab :3")

moni = 0
order = input("what pizza would u like to order S, M or L: ")

if order == "S":
    order1 = print("would you like a extra cheese? Y, N:")
    if order1 == "Y":
        print(f"total is {moni} enjoy! ")
        
else:
    print("bye")