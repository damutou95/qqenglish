#删除纯中文文档
import os
s = os.listdir('/home/xiyujing/qqenglish/蛐蛐英语')
toBeremoved = []
for i in s:
    with open(f'/home/xiyujing/qqenglish/蛐蛐英语/{i}', 'r') as f:
        long = f.read()
    a = []

    for m in long:
        if ord(m) <256:
            a.append(m)
    if len(a) < len(long)*0.2:
        toBeremoved.append(f'/home/xiyujing/qqenglish/蛐蛐英语/{i}')
for n in toBeremoved:
    os.remove(n)