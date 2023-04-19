try:
    a,b,c = map(int, input().split())
    if a > b:
        a, b = b, a
    f = min(b-a, c) #最多替换f个
    c-=f #
    a+=f #把食材分配给最少的a
    a+=c // 2 #把c剩下的一半分配给a
    print(a // 2) #计算a、、2
except ValueError:
    print("我报错了")
except EOFError:
    print("检查一下内存吧")

