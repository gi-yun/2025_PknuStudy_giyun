import sys

def gugu(a=2, b=10):
    result = ""
    for i in range(a, b + 1):
        result += (f'====={i}단=====\n')
        for j in range(1, 10):
            result += (f'{i}x{j}={i*j}\n')
    return result

if len(sys.argv) < 3:
    print("Usage: python gugu.py <start> <end>")
    sys.exit(1)

value = sys.argv[1:]
x = int(value[0])
y = int(value[1])
print(gugu(x, y))

print(x)
print(y)