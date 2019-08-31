print(1)
total = 0
i = 3
while i <= 100:
    if i % 2 == 1:
    # if i % 2 != 1:为奇数
        print (i)
        total += i
    i += 1
total=total+1
print("0-100之间的求和是:%d" % total)
