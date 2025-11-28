a = int(input("Enter a value: "))

if a % 2 == 0:
    count = a - 1
else:
    count = a

result = []

for i in range(1, count + 1):
    odd = 2 * i - 1
    result.append(str(odd))

print(", ".join(result))
