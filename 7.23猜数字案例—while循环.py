# while循环设计猜数字.无限次机会，每次猜不中都会提示，猜完会提示猜测了几次
import random
num = random.randint(1,100)
guess_num = int(input("请猜测我想到数字是"))
frequency = 1
while guess_num != num:
    print(f"这是你的第{frequency}次")
    if guess_num < num:
        print("数字小了")
    else:
        print("数字大了")
    guess_num = int(input("这次猜错了，请继续猜测"))
    frequency += 1
if guess_num == num:
    print("恭喜你，第%d次就猜出来了" % frequency)

