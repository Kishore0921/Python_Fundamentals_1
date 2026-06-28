'''
Operators in Python are special symbols that carry out arithmetic or logical computation. 
The value that the operator operates on is called the operand.
Operators are used to perform operations on variables and values.
'''

#Declaring value for variables to access it 
a , b = 10 , 5

# Arthmetic Operators (+ - * / // % **)
print("Arithmetic Operators")
print("Addition of a and b is :", a + b)
print("Subtraction of a and b is :", a - b)
print("Multiplication of a and b is :", a * b)
print("Division of a and b is :", a / b) # Returns the quotient in floating value
print("Floor Division of a and b is :", a // b) # Returns the quotient in integer value
print("Modulus of a and b is :", a % b) # Returns the remainder
print("Exponentiation of a and b is (a raised to the power b):", a ** b) 

# Comparison Operators (== != > < >= <=)
print("\nComparison Operators")
print("Is a equal to b? :", a == b) # Returns True if a is equal to b, otherwise returns False
print("Is a not equal to b? :", a != b) # Returns True if a is not equal to b, otherwise returns False
print("Is a greater than b? :", a > b) # Returns True if a is greater than b, otherwise returns False
print("Is a less than b? :", a < b) # Returns True if a is less than b, otherwise returns False
print("Is a greater than or equal to b? :", a >= b)
print("Is a less than or equal to b? :", a <= b)

# Logical Operators (and or not) 
'''
and :- if any one is False it returns False. True if and only if both are True 
or :- if any one is True it returns True. False if and only if both are False
not :- converts True to False and False to True
'''
print("\n Logical operators") 
print("Is a greater than 5 and b less than 10? :", a > 5 and b < 10)
print("Is a greater than 5 or b less than 10? :", a > 5 or b < 10)
print("Is a not equal to 10? :", not (a == 10)) # Returns False because a is equal to 10 

# Bitwise Operators (& | ^ ~ << >>)
# Think of these numbers as patterns of 4 light switches:
x = 5  # In binary: 0101 
y = 3  # In binary: 0011 

print("\nBitwise Operators")
# 1. AND (&) Only keeps the 1s if BOTH numbers have a 1 in that spot.
# Rule: If switch x AND switch y are both 1, result is 1. Otherwise 0.
print("   5 & 3 =", x & y)  # 0101 & 0011 -> 0001 (which is 1)

# 2. OR (|) Keeps a 1 if AT LEAST ONE number has a 1 in that spot.
# Rule: If switch x OR switch y (or both) is 1, result is 1.
print("   5 | 3 =", x | y)  # 0101 | 0011 -> 0111 (which is 7)

# 3. XOR (^) Gives a 1 ONLY if the spots are different (one is 1, one is 0).
# Rule: If the bits are different, result is 1. If they are the same, result is 0.
print("   5 ^ 3 =", x ^ y)  # 0101 ^ 0011 -> 0110 (which is 6)

# 4. NOT (~) Flips all the switches to their exact opposite.
# Rule: It flips every bit. 1 becomes 0, and 0 becomes 1. 
# Shortcut formula for math: ~x is always equal to (-x - 1)
print("   ~5 =", ~x)  # Flips 5 into -6

# 5. Left Shift (<<) Shifts bits left. Shifting by 1 doubles the number.
# Rule: Moves all bits to the left. Moving 1 spot to the left doubles the number.
print("   5 << 1 =", x << 1)  # 5 becomes 10

# 6. Right Shift (>>) Shifts bits right. Shifting by 1 halves the number (rounds down).
# Rule: Moves all bits to the right. Moving 1 spot to the right cuts the number in half.
print("   5 >> 1 =", x >> 1)  # 5 becomes 2

# Assignment Operators (= += -= *= /= //= %= **=)
print("\nAssignment Operators")
x = 5
y = 3
x = y   ; print("Value of x is? :", x)  # Assigns y to x 
x = 5   ; x += y ; print("Value of x is? :", x)  # Adds y to x (Same as x = x + y)
x = 5   ; x -= y ; print("Value of x is? :", x)  # Subtracts y from x (Same as x = x - y)
x = 5   ; x *= y ; print("Value of x is? :", x)  # Multiplies x by y (Same as x = x * y)
x = 5   ; x /= y ; print("Value of x is? :", x)  # Divides x by y (Same as x = x / y)
x = 5   ; x %= y ; print("Value of x is? :", x)  # Finds remainder of x divided by y (Same as x = x % y)
