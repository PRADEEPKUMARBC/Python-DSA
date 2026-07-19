n = [2,1,3,5,7,1,9,3,10]
m = [10,111,2,3,4,5,6,7,8,35,97,1]

for num in m:
    count = 0
    for i in n:
        if i == num:
            count += 1
    print(num,count)

