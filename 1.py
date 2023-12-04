a = []
with open('1.txt', 'r') as file:
    for line in file:
        a.append(int(line))
print(a)
x = ''
for i in range(len(a) - 1):
    if a[i] % 3 == 0 or a[i + 1] % 3 == 0:
        x = x + str(a[i]) + ' ' + str(a[i + 1]) + ','
x = x.split(',')
print(len(x))
list_a = []
for i in range(len(x) - 1):
    a1, a2 = x[i].split(' ')
    list_a.append(int(a1) + int(a2))
print(max(list_a))
