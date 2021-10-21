import random

secret = random.randint(1,100)
print('''猜数字！我随机给出了1-100的整数，你最多可以猜10次''')
tries = 1
while tries <= 10:
    guess = int(input("第%d次猜数，请输入一个整数："%(tries,)))
    if guess==secret:
        print("恭喜答对了！你只用了%d次！\n就是这个：%d!"%(tries,secret))
        break
    elif guess>secret:
        print("不好意思，你的数大于答案")
    elif guess<secret:
        print("不好意思，你的数小于答案")
    tries+=1
else:
    print("尝试次数过多！再见！")
