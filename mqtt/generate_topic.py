import random

# 生成100行内容到文件中
with open('test.txt', 'w') as f:
    for i in range(100):
        # 生成随机6位字符串
        rand_str = ''.join([random.choice('abcdefghijklmnopqrstuvwxyz') for j in range(6)])
        # 写入文件，每行以换行符结束
        f.write(f"test/{rand_str}\n")

