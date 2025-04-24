a = 5
b = 3
print(a & b)  # Output: 1 (0101 & 0011 = 0001)

print(a | b)  # Output: 7 (0101 | 0011 = 0111)

print(a ^ b)  # Output: 6 (0101 ^ 0011 = 0110)

print(~a)  # Output: -6 (bitwise NOT of 5 is -6 in two's complement representation)
# normally ~5 = ~(101) = 010 but for number sign is strored in left most bit and when not operation is performed Sign bit is also inverted
# so it becomes (1)sign (010)number and python stores -ve numbers in two's complement form
# whats 2's complement?
# to understand 2's complement, first understand 1's complement
# 1's complement is the binary representation of a number where all bits are inverted (0 becomes 1 and 1 becomes 0).
# For example, the 1's complement of 5 (0101) is 1010.
# To find the 2's complement, you take the 1's complement and add 1 to it. So, for 5 (0101), the 2's complement is:
# 1010 + 1 = 1011, which is -5 in two's complement representation.

#  thats why if we perform ~5 = (0)Sign (101)number = (1)Sign (010)number  as sign is ->-ve we will take 2's complement of 010
# so 2's complement of 010 is 1010 + 1 = 1011 which is -6 in decimal

print(a << 1)  # Output: 10 (0101 << 1 = 1010, which is 10 in decimal)

print(a >> 1)  # Output: 2 (0101 >> 1 = 0010, which is 2 in decimal)