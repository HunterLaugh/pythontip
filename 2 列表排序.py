#coding:utf-8
'''
列表排序

给你一个列表 L, 对L进行升序排序并输出排序后的列表。

例如：L = [8,2,50,3]

则输出：[2,3,8,50]

'''
L=[99,77,32,11,-21,83,0]
L=[0,3,1,2]

# 解法二：冒泡排序，小的与大交换位置
n=len(L)
i=0
while i<n-1:
	j=i+1
	while j<n:
		if L[i]>L[j]:
			temp=L[i]
			L[i]=L[j]
			L[j]=temp
		print("i",i,"j",j,L)	
		j+=1
	i+=1
print(L)

# 解法一：每次提取最小的数据
#存放结果
res=[] 

while len(L)>0:
	min=L[0]
	for each in L:
		if  min>each:
			min=each
	res.append(min)
	L.remove(min)
	
#print(res)

