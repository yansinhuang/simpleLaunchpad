l = int(input())
w = int(input())

if (l*w) % 2 == 0:
    str = '+-'*((l*w)/2)
    print(str)