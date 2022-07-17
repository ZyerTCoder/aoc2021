G=[[*map(int,l.strip())]for l in open(0)]
L,R=len(G),range
S=L*L
def I(r,c,s,F):
 s[r][c]+=1
 if s[r][c]>9 and F[r][c]:
  F[r][c]=0
  for x in [r-1,r,r+1]:
   for y in [c-1,c,c+1]:
    if 0<=x<L and 0<=y<L:s,F=I(x,y,s,F)
 return s,F
i=f=0
while 1:
 i += 1
 F=[[1]*L for _ in R(L)]
 for n in R(S):G,F=I(n//L,n%L,G,F)
 for n in R(S):
  if G[n//L][n%L]>9:G[n//L][n%L]=0
 k=S-sum([sum(l) for l in F])
 f+=k
 if i==100:print(f)
 if k==S:print(i);