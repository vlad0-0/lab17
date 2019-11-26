a = []
k2 = int(input())
n = int(input())
for i in range(n):
  a.append(int(input()))
k1 = 1
l1 = 0
r1 = 1
i = 0
while i < n-1:
  if a[i] == a[i+1]:
    r1 += 1
  else:
    k1 += 1
    l1 = r1
    r1 += 1
  i += 1
  if k1 == k2:
      break
l2 = r1
r2 = r1+1
while i < n-1:
  if a[i] == a[i+1]:
    r2 += 1
  else:
    l2 = r2
    r2 += 1
  i += 1
a[l1:r1+1], a[l2-1:r2] = a[l2-1:r2], a[l1:r1+1]
print(a)
