a = []
with open('2.txt', 'r') as file:
    for line in file:
        a.append(int(line))
x = ''
for i in range(len(a) - 1):
    for u in range(i+1,len(a)):
        if (a[i]%160 != a[u]%160) and ((a[i] % 7 == 0) or (a[u] % 7 == 0)):
            x = x + str(a[i]) + ' ' + str(a[i + 1]) + ','
x = x.split(',')
print(x)
list_a = []
for i in range(len(x) - 1):
    a1, a2 = x[i].split(' ')
    list_a.append(int(a1) + int(a2))
print(list_a)
print(len(x),max(list_a))