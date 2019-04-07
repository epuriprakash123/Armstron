N=int(input())
sum=0
tmp=N
while(tmp>0):
	c=tmp%10
	sum+=c**3
	tmp//=10
if(N==sum):
	print("yes")
else :
	print("no")
