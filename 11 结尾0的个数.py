'''
给你一个正整数列表 L, 输出L内所有数字的乘积末尾0的个数。(提示:不要直接相乘,数字很多,相乘得到的结果可能会很大)。

例如： L=[2,8,3,50],

则输出：2
'''
# 正整数>0

#　0即10，质因子中2与5的个数
# 统计2与5作为质因子的次数
i5=0
i2=0

for each in L:
	while each%5==0:
		i5+=1
		each=each//5
	while each%2==0:
		i2+=1
		each=each//2

if i5>i2:
	res=i2
else:
	res=i5
print(res)
