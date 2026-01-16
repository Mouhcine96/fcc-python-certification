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
