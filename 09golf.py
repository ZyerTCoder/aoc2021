g=[[*map(int,l.strip())]for l in open(0)]
r,L,Q,p,*Z=range,len(g),len(g[1]),0
M=[[1]*Q for _ in r(L)]
A=lambda x,y:0<=x<L and 0<=y<Q
B=lambda x,y:[(x,y+1),(x+1,y),(x,y-1),(x-1,y)]
C=lambda x,y,m:[m[x][y]+1,0][any([A(r,c)and m[r][c]<=m[x][y] for r,c in B(x,y)])]
def F(x,y,g):
 o=1
 for r,c in B(x,y):
  if A(r,c)and g[r][c]!=9 and M[r][c]:M[r][c]=0;o+=F(r, c, g)
 return o
for n in r(L*Q):
 x,y=n//Q,n%Q
 if z:=C(x,y,g):p+=z
 if g[x][y]==9:M[x][y]=0
 elif M[x][y]:M[x][y]=0;Z+=[F(x, y, g)] 
Z.sort()
*_,a,b,c=Z
print(p,a*b*c)