# coding:utf-8
'''
5 输出字符奇数位置的字符串.py
给你一个字符串 a， 输出a中奇数位置字符构成的字符串（位置编号从1开始）。

例如：a=‘xyzwd’

则输出:xzd

'''
 a=‘xyzwd’
 
res=[]
i=0
while i<len(a):
	if i%2==0:
		res.append(a[i])
	i+=1
print(''.join(res))