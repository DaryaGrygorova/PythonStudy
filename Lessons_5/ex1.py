res = [x for x in range(0,600, 6) if x % 7 == 0]
print(res)

new_list =[]
for item in range(10):
    new_list.append(item**0.5)

new_list = [item**0.5 for item in range(10)]