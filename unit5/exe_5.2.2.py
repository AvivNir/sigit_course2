
numbers = iter(list(range(1, 101)))  # skip the first number
for i in range(99):
    try:
        next(numbers)
        next(numbers)
        print(next(numbers))
    except StopIteration:
        print("done")
        break

