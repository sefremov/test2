import sys

# Function annotations
def f(a: int, b: int) -> int:
    return a + b


print(sys.argv)
a = sys.argv[1]
b = sys.argv[2]
print(f(a, b))