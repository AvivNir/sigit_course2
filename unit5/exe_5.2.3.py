import itertools
money_type = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
count_100 = 0
for i in range(5, 20):
    hundred = set(itertools.combinations(money_type, i))
    for item in hundred:
        if sum(item) == 100:
            print(item)
            count_100 += 1
print("there are only " + str(count_100) + " ways to create a sum of 100 with these bills")