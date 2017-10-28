# coding:utf-8
'''
给你一个字符串 a， 请你输出逆序之后的a。

例如：a=‘xydz’

则输出：zdyx

'''

# 解法一：
n=len(a)
i=0
li=[]
while i<n:
	li.insert(0,a[i])
	i+=1
res=''.join(li)
print(res)

# 解法二：：
liA=list(a)
newA=[]
while liA:
	newA.append(liA.pop())
print(''.join(newA))
	