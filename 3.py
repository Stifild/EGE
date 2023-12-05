a = []
with open('3.txt', 'r') as file:
    for line in file:
        a.append(int(line))
x = ''
for i in range(len(a) - 1):
    for u in range(i+1,len(a)):
        if abs(a[i] - a[i + 1]) % 2 == 0 or a[i + 1] % 31 == 0 or a[i] % 31 == 0:
            x = x + str(a[i]) + ' ' + str(a[i + 1]) + ','
x = x.split(',')
list_a = []
for i in range(len(x) - 1):
    a1, a2 = x[i].split(' ')
    list_a.append(int(a1) + int(a2))
print(len(x),max(list_a))
