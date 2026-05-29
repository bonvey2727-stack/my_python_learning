# while示例
# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# nwlist = []
# index = 0
# while index < len(mylist):
#     num = mylist[index]
#     if num % 2 == 0:
#         nwlist.append(num)
#
#     index += 1
#
# print(f"新列表是：{nwlist}")

# for示例
# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# nwlist = []
# for index in mylist:
#     if index % 2 == 0:
#         nwlist.append(index)
#
#     index += 1
#
# print(f"新列表是：{nwlist}")



# 元组的基本操作
t1 = ("周杰伦", 11, ["football", "music"])
# 查询年龄所在的下标位置
index = t1.index(11)
# 查询学生的姓名
name = t1[0]
# 删除爱好中的football
t1[2].remove("football")
# 把coding加入到爱好中
t1[2].append("coding")

print(index)
print(name)
print(t1)









