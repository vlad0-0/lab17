a = []
b = int(input())
n = int(input())
for i in range(n):
  a.append(int(input()))
l = 0
r = 1
a.append(0.5)
for i in range(n):
  if a[i] == a[i+1]:
    r += 1
  else:
    if r-l >= b:
      for j in range(l, r):
          a[j] = 0
      l = r
      r += 1
    else:
      l = r
      r += 1
del(a[-1])
print(a)
