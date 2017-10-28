# coding:utf-8
'''
4 输出字典key
给你一字典a，如a={1:1,2:2,3:3}，输出字典a的key，以','连接，如‘1,2,3'。要求key按照字典序升序排列(注意key可能是字符串）。

例如：a={1:1,2:2,3:3}, 则输出：1,2,3

'''

a={1:1,2:2,3:3}

# 获取dict keys
a_keys=a.keys()

#　排序
a_keys.sort()

#　连接
res=','.join(a_keys)

print(res)