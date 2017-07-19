import os
path = input("输入路径：")
for root,dirs,filenames in os.walk(path):
    for name in filenames:
        print(os.path.join(root,name))