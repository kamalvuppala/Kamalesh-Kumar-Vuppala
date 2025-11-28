a = int(input("Enter a value: "))

result = []

for i in range(1, a + 1):
    odd_num = 2 * i - 1
    result.append(str(odd_num))

print(", ".join(result))
