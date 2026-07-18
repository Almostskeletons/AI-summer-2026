print('以下是九九乘法表\n')
for n in range(1,10):
    for m in range(1,n+1):
        ans=n*m
        print(f'{m}*{n}={ans}',end='  ')
    print()
