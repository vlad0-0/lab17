a = []
n = int(input())
for i in range(n):
  a.append(list(map(int, input().split())))
x = 0
y = 0
for i in range(n):
  if a[i][0] < 0 and  a[i][1] > 0 and a[i][0]*a[i][0]+a[i][1]*a[i][1]> x*x+y*y:
    x = a[i][0]
    y = a[i][1]
print(x, y)
