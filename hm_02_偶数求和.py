# total = 0
# i = 0
# while (i % 2 == 0) & (i <= 100):
#      print(i)
#      total += i
#      i += 2
# print("0到100之间的偶数和为:%d" % total)

# way2:
total = 0
i = 0
while i <= 100:
    if i % 2 == 0:
        print(i)
        total += i
    i += 1
print("0到100之间的偶数和为:%d" % total)