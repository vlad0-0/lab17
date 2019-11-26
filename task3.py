a = []
k2 = int(input())
n = int(input())
for i in range(n):
  a.append(int(input()))
k1 = 1
for i in range(n):
  if a[i] == a[i+1]:
