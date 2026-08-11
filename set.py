# Set of 10 fruits
fruits = {
    "Apple", "Mango", "Banana", "Orange", "Grapes",
    "Watermelon", "Guava", "Pineapple", "Papaya", "Strawberry"
}

# Summer fruits
summer_fruits = {
    "Mango", "Banana", "Watermelon", "Papaya", "Pineapple"
}

# Winter fruits
winter_fruits = {
    "Apple", "Orange", "Grapes", "Guava", "Strawberry"
}

# 1. Print the name of all fruits in 3 sets
all_fruits = fruits | summer_fruits | winter_fruits
print("All fruits:", all_fruits)


# 2. Present in both Summer and Winter
both = summer_fruits & winter_fruits
print("2. Present in both:", both)

# 3. Present only in Summer but not in fruits
only_summer = summer_fruits - fruits
print("3. Only Summer, not in fruits:", only_summer)

# 4. Present in Summer and Winter and fruits
both_in_fruits = summer_fruits & winter_fruits & fruits
print("4. Summer and Winter and fruits:", both_in_fruits)

# 5. Check Orange
if "Orange" in fruits:
    print("5. Orange is present in fruits")
else:
    print("5. Orange is not present in fruits")

# 6. Find Pineapple
print("6. Pineapple is present in:")

if "Pineapple" in fruits:
    print("Fruits set")

if "Pineapple" in summer_fruits:
    print("Summer fruits set")

if "Pineapple" in winter_fruits:
    print("Winter fruits set")