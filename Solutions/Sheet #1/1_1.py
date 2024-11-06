# Section 1: Arithmetic expressions, types, and variables

# 1.1
# For each of the following expressions write the order in which it is evaluated.

# Execution order
# 1: Exponentiation (**): Evaluering fra højre mod venstre.
# 2: Multiplication (*), Division (/), Floor Division (//), og Modulus (%): Evaluering fra venstre mod højre.
# 3: Addition (+) og Subtraction (-): Evaluering fra venstre mod højre.


# 1.1.a
a + b * c**d
# 1. c ** d evalueres først (eksponentiation).
# 2. Derefter b * (c ** d) (multiplikation).
# 3. Til sidst a + (b * (c ** d)) (addition).

# 1.1.b
a + b**c * d
# 1. b ** c evalueres først (eksponentiation).
# 2. Derefter b ** c * d (multiplikation).
# 3. Til sidst a + (b ** c * d) (addition).

# 1.1.c
a / b // c * d
# 1. a / b evalueres først (division).
# 2. Derefter a / b // c (floor division).
# 3. Til sidst (a / b // c) * d (multiplikation).

# 1.1.d
a + b - c - d
# 1. a + b evalueres først (addition).
# 2. Derefter a + b - c (subtraction).
# 3. Til sidst (a + b - c) - d (subtraction).

# 1.1.e
a**b - c**d
# 1. a ** b evalueres først (eksponentiation).
# 2. Derefter a ** b - c ** d (subtraction).

# 1.1.f
a**b**c - d
# 1. b ** c evalueres først (eksponentiation).
# 2. Derefter a ** (b ** c) (eksponentiation).
# 3. Til sidst a ** (b ** c) - d (subtraction).

# 1.1.g
a / b - c * d
# 1. a / b evalueres først (division).
# 2. Derefter a / b - c (subtraction).
# 3. Til sidst (a / b - c) * d (multiplikation).

# 1.1.h
a * b**c * d
# 1. b ** c evalueres først (eksponentiation).
# 2. Derefter a * (b ** c) (multiplikation).
# 3. Til sidst a * (b ** c) * d (multiplikation).

# 1.1.i
a % b / c**d
# 1. a % b evalueres først (modulus).
# 2. Derefter a % b / c (division).
# 3. Til sidst (a % b / c) ** d (eksponentiation).


# 1.1.j
a - b - -c - --d
# 1. -c evalueres først (negation).
# 2. --d evalueres derefter (negation).
# 3. Derefter a - b - -c (subtraction).
# 4. Til sidst (a - b - -c) - --d (subtraction).
