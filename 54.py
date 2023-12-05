a = []
with open('54.txt', 'r') as file:
    for line in file:
        a.append(int(line))


def len_int(int):
    return len(str(int))


def len_chek(n1, n2, n3):
    if len_int(n1) == 5 and len_int(n2) == 5 and len_int(n3) != 5:
        return True
    if len_int(n1) != 5 and len_int(n2) == 5 and len_int(n3) == 5:
        return True
    if len_int(n1) == 5 and len_int(n2) != 5 and len_int(n3) == 5:
        return True


x = ''
for i in range(len(a) - 2):
    if len_chek(a[i], a[i + 1], a[i + 2]) and a[i] + a[i + 1] + a[i + 2] <= max(a):
        x = x + str(a[i]) + ' ' + str(a[i + 1]) + ' ' + str(a[i + 2])
x = x.split(',')
list_a = []
for i in range(len(x) - 1):
    a1, a2 = x[i].split(' ')
    list_a.append(int(a1) + int(a2))
print(len(x)-1,max(list_a))

