my_list = ["黑马程序员", "传智教育", "黑马程序员", "传智教育", "itheima", "itcast", "itheima", "itcast", "best"]
my_set = set()
# 通过for循环遍历列表
for eletment in my_list:
    # 将列表的元素添加至集合
    my_set.add(eletment)

print(my_set)

# 更简便的办法
my_set = set(my_list)