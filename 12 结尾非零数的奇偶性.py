'''
给你一个正整数列表 L, 判断列表内所有数字乘积的最后一个非零数字的奇偶性。
如果为奇数输出1,
偶数则输出0.。

例如：L=[2,8,3,50]

则输出：0

最后一个非零数字的奇偶性
'''

# 最后一个非零的奇偶性，转化成求质因子2与5的个数
i5=0
i2=0

for each in L:
	while each%5==0:
		i5+=1
		each=each//5
	while each%2==0:
		i2+=1
		each=each//2

# i5==i2 奇数
if i5>=i2:
	res=1
else:
	res=0

print(res)