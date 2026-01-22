# String basics and immutability

greeting = "Hello"
name = "Mouhcine"

print(greeting, name)

# Quotes inside strings
msg = "It's a sunny day"
quote = 'She said, "Hello!"'
print(msg)
print(quote)

# in operator
text = "Hello world"
print("Hello" in text)
print("hi" in text)

# Length and indexing
print(len(text))
print(text[0])
print(text[-1])

# Immutability example
greeting = "hi"
greeting = "hello"
print(greeting)

# This would fail:
# greeting[0] = "H"

# String concatenation

first_name = "Mouhcine"
age = 29

concat = first_name + " " + str(age)
print(concat)

# Augmented assignment
text = first_name
text += " "
text += str(age)
print(text)

# f-string interpolation
info = f"My name is {first_name} and I am {age} years old"
print(info)

# Expression in f-string
a = 20
b = 10
print(f"The sum of {a} and {b} is {a + b}")

# String slicing

text = "Hello world"

print(text[1:4])    # ell
print(text[:7])     # Hello w
print(text[8:])     # rld
print(text[:])      # Hello world

# Step parameter
print(text[0:11:2]) # Hlowrd

# Reverse string
print(text[::-1])   # dlrow olleH

# =========================
# Common String Methods
# =========================

text = "  hello world  "

print("Original:", text)

# strip() – remove leading/trailing whitespace
clean = text.strip()
print("strip():", clean)

# upper() / lower()
print("upper():", clean.upper())
print("lower():", clean.lower())

# capitalize() / title()
print("capitalize():", clean.capitalize())
print("title():", clean.title())

# replace()
print("replace():", clean.replace("world", "Python"))

# split()
words = clean.split()
print("split():", words)

# join()
joined = "-".join(words)
print("join():", joined)

# startswith() / endswith()
print("startswith('hello'):", clean.startswith("hello"))
print("endswith('world'):", clean.endswith("world"))

# find()
print("find('world'):", clean.find("world"))

# count()
print("count('l'):", clean.count("l"))

# isupper() /
