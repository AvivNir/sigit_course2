def parse_ranges(ranges_string):
    ranges = (range(int(start), int(stop) + 1)
              for start, stop in (pair.split('-')
                                  for pair in ranges_string.split(',')))
    return (num for subrange in ranges for num in subrange)


if __name__ == '__main__':
    print(list(parse_ranges("1-2,4-4,8-10")))
    print(list(parse_ranges("0-0,4-8,20-21,43-45")))