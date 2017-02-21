import re

'''
请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：
someone@gmail.com
bill.gates@microsoft.com

版本二可以验证并提取出带名字的Email地址：
<Tom Paris> tom@voyager.org
'''
re_email=re.compile(r'^([\w\_\.]+)\@([\w\_\.]+)$')
re_email2=re.compile(r'^<(\w+\s?\w+)>\s([\w\_\.]+)\@([\w\_\.]+)$')

#test
#email=input('输入邮箱：')
email = 'bill.gates@microsoft.com'
getresult=re_email.match(email).groups()
print(getresult)

email2 = '<Tom Paris> tom@voyager.org'
getresult2=re_email2.match(email2).groups()
print(getresult2)
