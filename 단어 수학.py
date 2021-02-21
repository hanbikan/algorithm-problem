a,R,m,N=[0]*26,0,9,int(input())
for i in range(N):
    l=input()
    for j in range(len(l)): a[ord(l[j])-65]+=10**(len(l)-j-1)
a.sort(reverse=True)
for t in a: R,m=R+t*m,m-1
print(R)