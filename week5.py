animals = ["dogs", "cats", "birds", "whales", "raccoons", "squirrels"]
print(animals)

items1and2 = animals[0:2]
items3and4 = animals[2:4]
print("The first two items in the list are:", items1and2[0], ",", items1and2[1])
print("The middle two items in the list are:", items3and4[0], ",", items3and4[1])
print("The first and last items in the list are: ", animals[0],",", animals[-1])

menu = ("Ravioli","Gnocchi", "Linguine","Lasagna", "Spaghetti")
print("First Menu:")
for food in menu:
    print(food)

new_menu = ("Ravioli","Gnocchi", "Linguine","Pizza", "Alfredo")
print("New Menu:")
for food in new_menu:
    print(food)

# animals[0] = "kangaroos"
# animals.insert(1,"hedgehogs")
# print(animals)
# animals.append("bears")
# print(animals)
# print(animals.pop())
# print(animals)
# animals.sort()
# print(animals)
# print(len(animals))

# for animalbaby in animals:
#     print("Do you like " + animalbaby)
#     print("I do too!")

# print("Finished")

# numbers = list(range(1,10))
# print(numbers)

# for number in numbers:
#         square = number**2
#         print(square)

# ns1 = numbers[2:3] 
# ns2 = numbers[0:9:2]
# print(ns1)
# print(ns2)


# numbers2 = numbers
# numbers2.append(10)
# print(numbers2)
# print(numbers)

# # animals = ("dogs", "cats", "birds", "whales", "raccoons")
# # print(animals)