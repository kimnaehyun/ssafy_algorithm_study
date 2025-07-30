s = input()
tes = set()
for i in range(len(s)) :
    for j in range(len(s) + 1) :
        if j > i :
            tes.add(s[i:j])
print(len(tes))