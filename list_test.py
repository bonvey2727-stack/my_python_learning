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



# # 元组的基本操作
# t1 = ("周杰伦", 11, ["football", "music"])
# # 查询年龄所在的下标位置
# index = t1.index(11)
# # 查询学生的姓名
# name = t1[0]
# # 删除爱好中的football
# t1[2].remove("football")
# # 把coding加入到爱好中
# t1[2].append("coding")
#
# print(index)
# print(name)
# print(t1)


# str = "itheima itcast boxuegu"
# count = str.count("it")
# print(f"字符串中有{count}个it")
# new_str = str.replace(" ", "|")
# print(new_str)
# new_str2 = new_str.split("|")
# print(new_str2)


str = "万过薪月， 员序程马黑来， nohtyP学"
# 方法一
str1 = str[10:5:-1]
print(str1)
# 方法二
str2 = str.split("，")
str3 = str2[1].replace("来", "")
str4 = str3[::-1]
print(str4)

str5 = str.split("，")[1].replace("来", "")[::-1]
print(str5)