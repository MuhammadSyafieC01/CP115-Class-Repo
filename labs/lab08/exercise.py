"""

# Test addition and subtraction
result1 = 25 + 15
result2 = 100 - 25
print(f"25 + 15 = {result1}")
print(f"100 - 25 = {result2}")

# Test multiplication and division
result3 = 8 * 7
result4 = 20 / 4
print(f"8 * 7 = {result3}")
print(f"20 / 4 = {result4}")

# Test floor division, modulus, and powers
result5 = 17 // 5
result6 = 17 % 5
result7 = 3 ** 4
print(f"17 // 5 = {result5}")
print(f"17 % 5 = {result6}")
print(f"3 ** 4 = {result7}") """

# Test division - always returns float
division = 10 / 2
print(f"10 / 2 = {division} (type: {type(division)})")

# Test floor division - returns int when both operands are int
floor_div = 10.5 // 3
print(f"10 // 3 = {floor_div} (type: {type(floor_div)})")

# Test modulus - returns int when both operands are int
modulus = 17 % 5
print(f"17 % 5 = {modulus} (type: {type(modulus)})")

# Test exponentiation - returns int when both operands are int
power = 2 ** 3
print(f"2 ** 3 = {power} (type: {type(power)})")