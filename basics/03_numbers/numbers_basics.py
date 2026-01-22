# =========================
# Numbers: Integers & Floats
# =========================

# Integers
a = 56
b = 12

print("Integer addition:", a + b)
print("Integer subtraction:", a - b)
print("Integer multiplication:", a * b)
print("Integer division:", a / b)  # always float

# Floats
x = 5.4
y = 12.0

print("Float addition:", x + y)
print("Float subtraction:", y - x)
print("Float multiplication:", y * x)
print("Float division:", y / x)

# Mixed types → float result
result = a + x
print("Int + Float:", result, type(result))

# Modulo (remainder)
print("Modulo int:", a % b)
print("Modulo float:", y % x)

# Floor division
print("Floor division int:", a // b)
print("Floor division float:", y // x)

# Exponentiation
print("Exponentiation int:", a ** 2)
print("Exponentiation float:", x ** 2)

# Type conversion
print("int to float:", float(a))
print("float to int:", int(x))  # cuts off decimals

# String to number
num_str_int = "45"
num_str_float = "7.8"

print(int(num_str_int), type(int(num_str_int)))
print(float(num_str_float), type(float(num_str_float)))

# Built-in functions
print("round():", round(4.798))
print("round(1 decimal):", round(4.253, 1))
print("abs():", abs(-15))
print("pow():", pow(2, 3))
print("pow with modulo:", pow(2, 3, 5))
