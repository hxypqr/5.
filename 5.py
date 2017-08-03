x=[1]
a="swsdxxxxxxxxxxdasgsfedadss"
t=len(a)
print t
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
          x.append(a[i:j+1])
print x
y="a"
t=len(x)
print t
x.pop(0)
print x
for l in range(-1,t-1):
    if len(y)<len(x[l]):
        y=x[l]

print y
