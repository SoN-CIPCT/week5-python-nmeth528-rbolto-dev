animals = ["dogs", "cats", "birds", "whales", "raccoons", "squirrels"]
print("List of six animals:")
for animal in animals:
    print(animal)

items1and2 = animals[0:2]
items3and4 = animals[2:4]

print()

print(f"The first two items in the list are: {items1and2[0]}, {items1and2[1]}")
print(f"The middle two items in the list are: {items3and4[0]}, {items3and4[1]}")
print(f"The first and last items in the list are: {animals[0]}, {animals[-1]}")

print()

menu = ("Ravioli","Gnocchi", "Linguine","Lasagna", "Spaghetti")
print("First Menu:")
for food in menu:
    print(food)

print()

new_menu = ("Ravioli","Gnocchi", "Linguine","Pizza", "Alfredo")
print("New Menu:")
for food in new_menu:
    print(food)

