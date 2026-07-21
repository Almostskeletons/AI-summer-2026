#factorial
def muttiply(n):
    if n==0:
        return 1
    else:
        return n*muttiply(n-1)
put=int(input("请输入一个数字n:"))
ans=muttiply(put)
print(f"我计算出来了{ans}")



#fibonacci
def fibonacci(n):
    """返回第n个斐波那契数（从1开始）"""
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def sum_fibonacci(n):
    """求前n个斐波那契数的和"""
    total = 0
    for i in range(1, n + 1):
        total += fibonacci(i)
    return total

# 主程序
n = int(input("请输入数字n: "))
result = sum_fibonacci(n)
print(f"前{n}个斐波那契数的和是: {result}")
