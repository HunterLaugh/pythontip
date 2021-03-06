'''
银行在打印票据的时候，常常需要将阿拉伯数字表示的人民币金额转换为大写表示，现在请你来完成这样一个程序。

在中文大写方式中，0到10以及100、1000、10000被依次表示为：    零 壹 贰 叁 肆 伍 陆 柒 捌 玖 拾 佰 仟 万

以下的例子示范了阿拉伯数字到人民币大写的转换规则：

1	壹圆

11	壹拾壹圆

111	壹佰壹拾壹圆

101	壹佰零壹圆

-1000	负壹仟圆

1234567	壹佰贰拾叁万肆仟伍佰陆拾柒圆

现在给你一个整数a(|a|<100000000), 请你打印出人民币大写表示.

例如：a=1

则输出：壹圆

注意：请以Unicode的形式输出答案。提示：所有的中文字符，在代码中直接使用其Unicode的形式即可满足要求，中文的Unicode编码可以通过如下方式获得：u'壹'。

注意：代码无需声明编码！！不要在代码头部声明文件编码，否则会导致语法错误！

Note：数据已于2013-11-19日加强，原来通过的代码可能不能再次通过。

'''
a=123456

# dict字典处理
# 零 壹 贰 叁 肆 伍 陆 柒 捌 玖 拾
rmb_dict={0:'零',1:'壹',2:'贰',3:'叁',4:'肆',5:'伍',6:'陆',7:'柒',8:'拐',9:'玖'}

# 位数a<100,000,000　最高8位数
digit={8:'仟万',7:'佰万',6:'拾万',5:'万',4:'仟',3:'佰',2:'拾',1:'圆'}

li_a=list(str(a))
n=len(li_a)

# 1 2 3-->转换成汉字
res_a=[]
for each in li_a:
	res_a.append(rmb_dict[int(each)])
print(res_a)
	
# 位数转换成个十佰仟万	
res_b=[]
for each in range(n):
	res_b.append(digit[n-each])
print(res_b)

