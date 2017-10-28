'''
给你两个正整数a和b， 输出它们的最大公约数。

例如：a = 3, b = 5

则输出：1
'''
a=34
b=7

# 公约数
def divisor(x):
	divisors=[1]
	miu=int(x**0.5)+2
	for each in range(2,miu):
		while x%each==0:
			divisors.append(each)
			x=x//each
	divisors.append(x)
	return divisors
#print(divisor(34))


# 求约数的合集，并相乘为最大公约数	
li_a=divisor(a)
li_b=divisor(b)
res=1
for each in li_a:
	if each in li_b:
		res*=each	
		li_b.remove(each)
	
# 输出	
print(res)