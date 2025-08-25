import sys

n = int(sys.stdin.readline())
company = []

for _ in range(n):
    name, status = sys.stdin.readline().split()
    if status == "enter": company.append(name)
    else: company.remove(name)

for name in sorted(company, reverse=True): print(name)
