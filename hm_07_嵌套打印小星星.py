# 在控制台连续输出五行 `*`，每一行星号的数量依次递增:
# *
# **
# ***
# ****
# *****
# **开发步骤**
# * 1> 完成 5 行内容的简单输出
# * 2> 分析每行内部的 `*` 应该如何处理？
row = 1
while row <= 5:
    col = 1
    while col <= row:
       #print(col)
        print("*",end="")
        col += 1
    print("")
   # print("第%d行" % row)
    row += 1



