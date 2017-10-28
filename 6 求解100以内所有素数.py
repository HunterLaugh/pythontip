# coding:utf-8
'''
6 求解100以内所有素数.py
输出100以内的所有素数，素数之间以一个空格区分（注意，最后一个数字之后不能有空格）。

'''

# 素数只能被１和本身整除

# i控制2-100，只校验奇数
s='2'
for i in range(3,100):
	flag=0
	for j in range(2,i):
		if i%j==0:
			flag=1
			break
	if flag==0:
		s=s+' '+str(i)
print(s)		