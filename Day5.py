"""
找出所有水仙花数

Version: 0.1
Author: liyun
"""
for num in range(100,1000):
    low = num % 10
    mid = num // 10 % 10
    hig = num // 100
    if num == low **3 + mid ** 3 + hig ** 3:
        print(num)