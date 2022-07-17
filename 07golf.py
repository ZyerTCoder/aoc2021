i=sorted(map(int,next(open(0)).split(",")))
l=lambda x:x*(x+1)/2
p=q=0
for j in i:p+=abs(j-i[len(i)//2]);q+=l(abs(j-sum(i)//len(i)))
print(p,q)