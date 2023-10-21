# енгизуди сураймыз и утирмен блемез
u = input("Enter items separated by commas: ")
l = u.split(',')

# словарь кураймыз
d = {}
for i in l:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

# барин бирге жинаймыз
t = [(k, v) for k, v in d.items()]

# результатты шыгарамыз
print("Unique elements:", list(d.keys()))
print("Tuples with item frequencies:", t)