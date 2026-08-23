text = "python programming"

# 1. Display Python
print("1.", text[:6])

# 2. Display Programming
print("2.", text[7:])

# 3. Check Java and insert it if not present
if "java" not in text.lower():
    text = text.replace(" ", " java ")

print("3.", text)

# 4. Length of new string
print("4. Length:", len(text))

# 5. Count number of words
words = text.split()
print("5. Number of words:", len(words))

# 6. Capitalize each word
print("6.", text.title())

# 7. Remove all spaces
print("7.", text.replace(" ", ""))

# 8. Frequency of A, P, R, M
upper_text = text.upper()

print("8. Frequency:")
print("A =", upper_text.count("A"))
print("P =", upper_text.count("P"))
print("R =", upper_text.count("R"))
print("M =", upper_text.count("M"))