# L2是L1的排序（由小到大）
l1 = [4,5,7,1,3,9,0]
l2 = l1.copy()
l2.sort()
for i in range(len(l1)):
    print (l1[i],l2[i])
