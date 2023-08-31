for i in range(-2,2,4):
    print(i)

k = 0
for i in range(10):
	for j in range(3):
		k = k + i
print(k)

temp = []
for i in range(0, 10):
    if i % 2:
        continue
    temp.append(i)
print(temp)
print(sum(temp))

x = 10
for i in [1,2,3,4,5]:
    if i % 2 == 0:
        break
    x -= i
else:
    x = 10
print(x)