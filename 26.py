a = []
with open('26.txt', 'r') as file:
    for line in file:
        a.append(int(line))
print(a)
x = ''
for i in range(len(a) - 1):
    if (a[i] % 3 == 0 or a[i + 1] % 3 == 0) and ((a[i]+a[i+1])%5==0):
        x = x + str(a[i]) + ' ' + str(a[i + 1]) + ','
x = x.split(',')
list_a = []
for i in range(len(x) - 1):
    a1, a2 = x[i].split(' ')
    list_a.append(int(a1) + int(a2))
print(len(x)-1,max(list_a))
