import string

s = input("请输入一行字符：")
letter = 0
space=0
digit=0
other=0
for c in s:
    if c.isalpha():
        letter+=1
    elif c.isspace():
        space+=1
    elif c.isdigit():
        digit+=1
    else:
        other+=1
print('你输入的字符串里有%d字母，%d个空格，%d个数字\
和%d个其他字符格式。'%(letter,space,digit,other))
