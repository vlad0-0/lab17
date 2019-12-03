n = int(input())
a = []
b = [0, 0, 0]
for i in range(n):
  a.append(list(map(int, input().split())))
pmax = 0
for i in range(n):
  for j in range(i+1, n):
    for k in range(j+1, n):
      s1 = ((a[i][0]-a[j][0])**2+(a[i][1]-a[j][1])**2)**0.5
      s2 = ((a[i][0]-a[k][0])**2+(a[i][1]-a[k][1])**2)**0.5
      s3 = ((a[j][0]-a[k][0])**2+(a[j][1]-a[k][1])**2)**0.5
      if pmax < s1+s2+s3:
        pmax = s1+s2+s3
        b[0] = a[i]
        b[1] = a[j]
        b[2] = a[k]
print(pmax)
print(b)
