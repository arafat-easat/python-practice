for i in range(3):
    print("I want to be a great Engineer")

for i in range(5):
    print(i)

print("<-----max_n------>")
numbers = [4, 0, 6, 18, 3, 9, 2]
max_n = numbers[0]
for n in numbers:
    if n > max_n:
        max_n = max(max_n, n)
print(max_n)
