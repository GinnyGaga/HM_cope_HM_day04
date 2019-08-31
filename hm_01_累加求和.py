i = 0
total = 0
while i <= 100:
    print(i)
    total += i
    #如果不先执行total运算，则total结果就会多出一个。
    i += 1
print ("0到100之间所有数字的累加和为:%d" % total)